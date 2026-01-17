#!/usr/bin/env python3
"""
Small local web UI for running ELx808 workflows.
"""

from __future__ import annotations

import datetime as _dt
import json
import os
import queue
import sys
import threading
import urllib.parse
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from subprocess import PIPE, STDOUT, Popen


ROOT_DIR = Path(__file__).resolve().parent
CONTROL_STACK = ROOT_DIR / "control_stack.py"


class RunState:
    def __init__(self, run_id: str, cmd: list[str], paths: dict[str, str]):
        self.run_id = run_id
        self.cmd = cmd
        self.paths = paths
        self.lines: list[str] = []
        self.queue: "queue.Queue[str | None]" = queue.Queue()
        self.process: Popen[str] | None = None
        self.started_at = _dt.datetime.now()
        self.ended_at: _dt.datetime | None = None
        self.returncode: int | None = None

    def to_dict(self) -> dict:
        return {
            "id": self.run_id,
            "cmd": self.cmd,
            "paths": self.paths,
            "started_at": self.started_at.isoformat(),
            "ended_at": self.ended_at.isoformat() if self.ended_at else None,
            "returncode": self.returncode,
        }


RUNS: dict[str, RunState] = {}
RUNS_LOCK = threading.Lock()


HTML = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>ELx808 Control Desk</title>
    <style>
      :root {
        --bg: #f6f1e9;
        --panel: #fff8f0;
        --ink: #1f1a14;
        --muted: #5c554c;
        --accent: #e85d3f;
        --accent-2: #1b8f8a;
        --line: #e3d7c9;
        --shadow: rgba(36, 28, 22, 0.12);
      }
      * { box-sizing: border-box; }
      body {
        margin: 0;
        font-family: "Avenir Next", "Avenir", "Gill Sans", "Trebuchet MS", sans-serif;
        color: var(--ink);
        background:
          radial-gradient(1200px 800px at 5% -10%, #ffe8d4 0%, transparent 60%),
          radial-gradient(1200px 800px at 110% 10%, #d9f3ef 0%, transparent 55%),
          linear-gradient(160deg, #f8f1e8 0%, #f7efe7 50%, #f4e9dc 100%);
        min-height: 100vh;
      }
      header {
        padding: 28px 32px 10px;
      }
      header h1 {
        margin: 0 0 6px 0;
        font-size: 28px;
        letter-spacing: 0.02em;
      }
      header p {
        margin: 0;
        color: var(--muted);
      }
      main {
        display: grid;
        grid-template-columns: minmax(280px, 380px) 1fr;
        gap: 24px;
        padding: 20px 32px 40px;
      }
      .panel {
        background: var(--panel);
        border: 1px solid var(--line);
        border-radius: 18px;
        box-shadow: 0 18px 50px var(--shadow);
        padding: 20px;
        animation: rise 0.6s ease both;
      }
      .panel h2 {
        margin: 0 0 16px 0;
        font-size: 18px;
      }
      .field {
        margin-bottom: 14px;
      }
      label {
        display: block;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: var(--muted);
        margin-bottom: 6px;
      }
      input, select, textarea {
        width: 100%;
        border: 1px solid var(--line);
        border-radius: 10px;
        padding: 10px 12px;
        font-size: 14px;
        background: #fffdf9;
        color: var(--ink);
      }
      .row {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 12px;
      }
      .toggle-row {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 12px;
        font-size: 13px;
      }
      .pill {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 6px 12px;
        border-radius: 999px;
        border: 1px solid var(--line);
        font-size: 12px;
        color: var(--muted);
      }
      .buttons {
        display: flex;
        gap: 12px;
        margin-top: 16px;
      }
      button {
        border: none;
        border-radius: 12px;
        padding: 12px 16px;
        font-weight: 600;
        cursor: pointer;
      }
      button.primary {
        background: var(--accent);
        color: #fff;
      }
      button.secondary {
        background: #f2e6d8;
        color: var(--ink);
      }
      .status {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 12px;
        color: var(--muted);
      }
      .status strong { color: var(--ink); }
      pre {
        background: #151311;
        color: #e9e0d3;
        border-radius: 14px;
        padding: 16px;
        height: 520px;
        overflow: auto;
        font-family: "IBM Plex Mono", "Menlo", "Courier New", monospace;
        font-size: 12px;
      }
      .badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 4px 10px;
        border-radius: 999px;
        font-size: 12px;
        background: rgba(27, 143, 138, 0.15);
        color: #0c5b58;
      }
      .warning {
        background: rgba(232, 93, 63, 0.14);
        color: #8f2c17;
      }
      @keyframes rise {
        from { opacity: 0; transform: translateY(12px); }
        to { opacity: 1; transform: translateY(0); }
      }
      @media (max-width: 980px) {
        main { grid-template-columns: 1fr; }
        pre { height: 380px; }
      }
    </style>
  </head>
  <body>
    <header>
      <h1>ELx808 Control Desk</h1>
      <p>Local UI wrapper for ECO60 validation and ECO590 live runs.</p>
    </header>
    <main>
      <section class="panel">
        <h2>Run Setup</h2>
        <div class="field">
          <label for="port">Serial Port</label>
          <input id="port" list="ports" placeholder="/dev/cu.usbserial-ABSCDEPH" />
          <datalist id="ports"></datalist>
        </div>
        <div class="field">
          <label for="mode">Mode</label>
          <select id="mode">
            <option value="validate-short-run">Validate Short Run (ECO60)</option>
            <option value="run-ecoplate">Run EcoPlate (ECO590)</option>
          </select>
        </div>
        <div class="row">
          <div class="field">
            <label for="profile">Profile</label>
            <input id="profile" value="ECO60" />
          </div>
          <div class="field">
            <label for="restore">Restore Profile</label>
            <input id="restore" value="ECO590" />
          </div>
        </div>
        <div class="row">
          <div class="field">
            <label for="csv">CSV Path</label>
            <input id="csv" />
          </div>
          <div class="field">
            <label for="manifest">Manifest Path</label>
            <input id="manifest" />
          </div>
        </div>
        <div class="field">
          <label for="log">Log Path</label>
          <input id="log" />
        </div>
        <div class="row">
          <div class="field">
            <label for="timeout">Timeout (sec)</label>
            <input id="timeout" type="number" min="0" step="1" placeholder="auto" />
          </div>
          <div class="field">
            <label for="quiet">Quiet (sec)</label>
            <input id="quiet" type="number" min="0" step="1" placeholder="auto" />
          </div>
        </div>
        <div class="toggle-row">
          <input id="strictComplete" type="checkbox" />
          <span>Strict terminator check</span>
        </div>
        <div class="toggle-row">
          <input id="noRestore" type="checkbox" />
          <span>Skip restore after short run</span>
        </div>
        <div class="toggle-row">
          <input id="confirm" type="checkbox" />
          <span>I confirm this will control the instrument.</span>
        </div>
        <div class="buttons">
          <button class="primary" id="startBtn">Start Run</button>
          <button class="secondary" id="stopBtn" disabled>Stop</button>
        </div>
        <p class="pill" id="runBadge">Idle</p>
      </section>
      <section class="panel">
        <div class="status">
          <span>Live Output</span>
          <span id="summary" class="badge">No run yet</span>
        </div>
        <pre id="output"></pre>
      </section>
    </main>
    <script>
      const output = document.getElementById("output");
      const runBadge = document.getElementById("runBadge");
      const summary = document.getElementById("summary");
      const startBtn = document.getElementById("startBtn");
      const stopBtn = document.getElementById("stopBtn");
      const modeSelect = document.getElementById("mode");
      let currentRunId = null;
      let eventSource = null;

      function ts() {
        const d = new Date();
        const pad = (n) => String(n).padStart(2, "0");
        return `${d.getFullYear()}${pad(d.getMonth()+1)}${pad(d.getDate())}-${pad(d.getHours())}${pad(d.getMinutes())}${pad(d.getSeconds())}`;
      }

      function setDefaults() {
        const stamp = ts();
        document.getElementById("csv").value = `/tmp/elx808-${stamp}.csv`;
        document.getElementById("manifest").value = `/tmp/elx808-${stamp}.json`;
        document.getElementById("log").value = `/tmp/elx808-${stamp}.log`;
      }

      function updateProfileDefaults() {
        const mode = modeSelect.value;
        if (mode === "run-ecoplate") {
          document.getElementById("profile").value = "ECO590";
        } else {
          document.getElementById("profile").value = "ECO60";
        }
      }

      async function loadPorts() {
        const list = document.getElementById("ports");
        list.innerHTML = "";
        try {
          const res = await fetch("/ports");
          const data = await res.json();
          for (const port of data.ports) {
            const opt = document.createElement("option");
            opt.value = port;
            list.appendChild(opt);
          }
        } catch (err) {
          console.warn("ports unavailable", err);
        }
      }

      function appendLine(line) {
        output.textContent += line + "\\n";
        output.scrollTop = output.scrollHeight;
      }

      function setRunState(state, detail) {
        runBadge.textContent = state;
        summary.textContent = detail || state;
        summary.className = "badge";
      }

      modeSelect.addEventListener("change", () => {
        updateProfileDefaults();
        setDefaults();
      });

      startBtn.addEventListener("click", async () => {
        if (!document.getElementById("confirm").checked) {
          alert("Please confirm instrument control before starting.");
          return;
        }
        if (currentRunId) {
          alert("A run is already active.");
          return;
        }
        const payload = {
          port: document.getElementById("port").value.trim(),
          mode: modeSelect.value,
          profile: document.getElementById("profile").value.trim(),
          restoreProfile: document.getElementById("restore").value.trim(),
          csv: document.getElementById("csv").value.trim(),
          manifest: document.getElementById("manifest").value.trim(),
          log: document.getElementById("log").value.trim(),
          timeout: document.getElementById("timeout").value.trim(),
          quiet: document.getElementById("quiet").value.trim(),
          strictComplete: document.getElementById("strictComplete").checked,
          noRestore: document.getElementById("noRestore").checked
        };
        if (!payload.port) {
          alert("Serial port is required.");
          return;
        }
        output.textContent = "";
        setRunState("Starting...", "Waiting for output");
        try {
          const res = await fetch("/run", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload),
          });
          if (!res.ok) {
            const err = await res.json();
            throw new Error(err.error || "Failed to start run");
          }
          const data = await res.json();
          currentRunId = data.id;
          startBtn.disabled = true;
          stopBtn.disabled = false;
          setRunState("Running", `Run ${data.id}`);
          eventSource = new EventSource(`/events/${data.id}`);
          eventSource.addEventListener("line", (ev) => {
            appendLine(ev.data);
          });
          eventSource.addEventListener("done", (ev) => {
            const msg = JSON.parse(ev.data);
            setRunState("Complete", `Return code: ${msg.returncode}`);
            startBtn.disabled = false;
            stopBtn.disabled = true;
            currentRunId = null;
            eventSource.close();
          });
        } catch (err) {
          setRunState("Error", err.message);
          startBtn.disabled = false;
          stopBtn.disabled = true;
          currentRunId = null;
        }
      });

      stopBtn.addEventListener("click", async () => {
        if (!currentRunId) return;
        await fetch(`/stop/${currentRunId}`, { method: "POST" });
        setRunState("Stopping...", "Sending terminate");
      });

      setDefaults();
      updateProfileDefaults();
      loadPorts();
    </script>
  </body>
</html>
"""


def _json_response(handler: BaseHTTPRequestHandler, payload: dict, status: int = 200) -> None:
    data = json.dumps(payload).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json")
    handler.send_header("Content-Length", str(len(data)))
    handler.end_headers()
    handler.wfile.write(data)


def _error(handler: BaseHTTPRequestHandler, message: str, status: int) -> None:
    _json_response(handler, {"error": message}, status)


def _list_ports() -> list[str]:
    return sorted(str(path) for path in Path("/dev").glob("cu.*"))


def _default_paths(run_id: str) -> dict[str, str]:
    stamp = _dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    base = f"/tmp/elx808-{run_id}-{stamp}"
    return {
        "csv": f"{base}.csv",
        "log": f"{base}.log",
        "manifest": f"{base}.json",
    }


def _build_command(data: dict) -> tuple[list[str], dict[str, str]]:
    if not data.get("port"):
        raise ValueError("port is required")
    mode = data.get("mode", "validate-short-run")
    profile = data.get("profile", "ECO60").strip() or "ECO60"
    paths = _default_paths(data.get("id", "run"))
    for key in ("csv", "log", "manifest"):
        if data.get(key):
            paths[key] = data[key]

    cmd = [
        sys.executable,
        str(CONTROL_STACK),
        "--port",
        data["port"],
        "--log",
        paths["log"],
        "--manifest",
        paths["manifest"],
    ]

    if data.get("timeout"):
        cmd += ["--timeout", str(data["timeout"])]
    if data.get("quiet"):
        cmd += ["--quiet", str(data["quiet"])]

    if mode == "run-ecoplate":
        cmd += ["run-ecoplate", "--confirm-run", "--csv", paths["csv"]]
        if profile:
            cmd += ["--profile", profile]
    else:
        cmd += ["validate-short-run", "--confirm-run", "--csv", paths["csv"]]
        if profile:
            cmd += ["--profile", profile]
        restore = data.get("restoreProfile", "ECO590").strip()
        if restore:
            cmd += ["--restore-profile", restore]
        if data.get("noRestore"):
            cmd += ["--no-restore"]
        if data.get("strictComplete"):
            cmd += ["--strict-complete"]
    return cmd, paths


def _run_worker(state: RunState) -> None:
    process = Popen(state.cmd, stdout=PIPE, stderr=STDOUT, text=True, bufsize=1)
    state.process = process
    assert process.stdout is not None
    for line in process.stdout:
        clean = line.rstrip("\n")
        state.lines.append(clean)
        state.queue.put(clean)
    process.wait()
    state.returncode = process.returncode
    state.ended_at = _dt.datetime.now()
    state.queue.put(None)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/":
            body = HTML.encode("utf-8")
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        if parsed.path == "/ports":
            _json_response(self, {"ports": _list_ports()})
            return
        if parsed.path.startswith("/runs/"):
            run_id = parsed.path.split("/")[-1]
            with RUNS_LOCK:
                state = RUNS.get(run_id)
            if not state:
                _error(self, "run not found", 404)
                return
            _json_response(self, state.to_dict())
            return
        if parsed.path.startswith("/events/"):
            run_id = parsed.path.split("/")[-1]
            with RUNS_LOCK:
                state = RUNS.get(run_id)
            if not state:
                _error(self, "run not found", 404)
                return
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "text/event-stream")
            self.send_header("Cache-Control", "no-cache")
            self.end_headers()

            def send_event(event: str, data: str) -> None:
                payload = data.splitlines() or [""]
                self.wfile.write(f"event: {event}\n".encode("utf-8"))
                for line in payload:
                    self.wfile.write(f"data: {line}\n".encode("utf-8"))
                self.wfile.write(b"\n")
                self.wfile.flush()

            for line in state.lines:
                send_event("line", line)
            while True:
                try:
                    item = state.queue.get(timeout=0.5)
                except queue.Empty:
                    if state.returncode is not None:
                        send_event("done", json.dumps({"returncode": state.returncode}))
                        break
                    continue
                if item is None:
                    send_event("done", json.dumps({"returncode": state.returncode}))
                    break
                send_event("line", item)
            return
        _error(self, "not found", 404)

    def do_POST(self) -> None:
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path.startswith("/stop/"):
            run_id = parsed.path.split("/")[-1]
            with RUNS_LOCK:
                state = RUNS.get(run_id)
            if not state or not state.process:
                _error(self, "run not found", 404)
                return
            state.process.terminate()
            _json_response(self, {"status": "terminating"})
            return
        if parsed.path != "/run":
            _error(self, "not found", 404)
            return
        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length) if length else b"{}"
        try:
            payload = json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError:
            _error(self, "invalid json", 400)
            return

        with RUNS_LOCK:
            active = any(state.process and state.returncode is None for state in RUNS.values())
        if active:
            _error(self, "another run is active", 409)
            return
        run_id = _dt.datetime.now().strftime("%H%M%S")
        payload["id"] = run_id
        try:
            cmd, paths = _build_command(payload)
        except ValueError as exc:
            _error(self, str(exc), 400)
            return
        state = RunState(run_id, cmd, paths)
        with RUNS_LOCK:
            RUNS[run_id] = state
        thread = threading.Thread(target=_run_worker, args=(state,), daemon=True)
        thread.start()
        _json_response(self, {"id": run_id, "paths": paths})


def main() -> int:
    host = "127.0.0.1"
    port = 8088
    server = ThreadingHTTPServer((host, port), Handler)
    print(f"ELx808 web UI running at http://{host}:{port}")
    print("Press Ctrl-C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
