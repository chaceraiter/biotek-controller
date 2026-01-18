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

try:
    import elx808_db
except ImportError:  # optional dependency
    elx808_db = None
import elx808_core as core
import serial_capture as sc


ROOT_DIR = Path(__file__).resolve().parent
CONTROL_STACK = ROOT_DIR / "control_stack.py"
ENV_PATH = ROOT_DIR.parent.parent / ".env"
STATE_DIR = Path(os.environ.get("ELX808_UI_STATE_DIR", "/tmp/elx808-ui"))
STATE_DIR.mkdir(parents=True, exist_ok=True)

DB = None
DB_ERROR = None

STATUS_312_CODES = {
    "0": "no fault or error",
    "8": "instrument failure - perform self-test",
    "9": "error in assay, scan, or table definition",
    "A": "error in well range selection",
    "B": "incubator setpoint error",
    "C": "incubator temperature error",
    "E": "barcode error",
}

TEST_TYPE_CODES = {
    "1": "FAIL POWER 5V",
    "2": "FAIL POWER 24V",
}

MOTOR_CODES = {
    "0": "Carrier X Axis",
    "1": "Filter Wheel",
    "2": "Robotic Door",
}

INCUBATOR_CODES = {
    "0": "Range Error",
    "1": "Thermistor Error",
    "2": "A/D Error",
}

DATA_FLASH_CODES = {
    "0": "Readback Error",
    "1": "Copy Error",
}

ELX_ERROR_RULES = [
    {"pattern": "0100", "label": "ABORT ERR", "detail": "read function aborted"},
    {"pattern": "020.", "label": "NO SENSOR ERR", "detail": "opto-sensor transition missing", "vars": [("motor", 3)]},
    {"pattern": "030.", "label": "NO BEAM ERR", "detail": "saturation transition missing", "vars": [("motor", 3)]},
    {"pattern": "040.", "label": "MOTOR VERIFY ERR", "detail": "positional verify failed", "vars": [("motor", 3)]},
    {"pattern": "050.", "label": "SATURATION ERR", "detail": "A/D signal saturated", "vars": [("test_type", 3)]},
    {"pattern": "060.", "label": "FILTER GAIN ERR", "detail": "filter gain out of range", "vars": [("filter", 3)]},
    {"pattern": "07.0", "label": "NOISE TEST ERR", "detail": "noise test failed", "vars": [("channel", 2)]},
    {"pattern": "08.0", "label": "OFFSET TEST ERR", "detail": "offset test failed", "vars": [("channel", 2)]},
    {"pattern": "09..", "label": "DARK RANGE ERR", "detail": "dark out of range", "vars": [("channel", 2), ("filter", 3)]},
    {"pattern": "0A..", "label": "AIR RANGE ERR", "detail": "air/blank out of range", "vars": [("channel", 2), ("filter", 3)]},
    {"pattern": "0B0.", "label": "ASSAY NUM ERR", "detail": "invalid assay number", "vars": [("assay", 3)]},
    {"pattern": "0C00", "label": "PRINT TIMEOUT ERR", "detail": "printer timed out"},
    {"pattern": "0D00", "label": "CAL CHECKSUM ERR", "detail": "calibration checksum failed"},
    {"pattern": "0E0.", "label": "WAVE NOT FOUND ERR", "detail": "wavelength missing", "vars": [("read_filter", 3)]},
    {"pattern": "0F..", "label": "FILTER SIGNAL ERR", "detail": "signal out of range", "vars": [("channel", 2), ("filter", 3)]},
    {"pattern": "1000", "label": "CNFG DATA ERR", "detail": "configuration data missing"},
    {"pattern": "1100", "label": "CNFG CHECKSUM ERR", "detail": "configuration checksum failed"},
    {"pattern": "1200", "label": "CAL DATA ERR", "detail": "calibration data missing"},
    {"pattern": "130.", "label": "MOTOR NOT HOMED ERR", "detail": "motor not homed", "vars": [("motor", 3)]},
    {"pattern": "15..", "label": "INCUBATOR FAILURE", "detail": "incubator failure", "vars": [("incubator_code", 2), ("zones", 3)]},
    {"pattern": "1600", "label": "SC ASSAY DEF ERR", "detail": "assay definition error"},
    {"pattern": "1700", "label": "KIN INTERVAL ERR", "detail": "kinetic interval too short"},
    {"pattern": "1800", "label": "KIN COUNT ERR", "detail": "too many kinetic intervals"},
    {"pattern": "1900", "label": "MALLOC ERR", "detail": "memory allocation failed"},
    {"pattern": "1A00", "label": "STORE CURVE ERR", "detail": "store curve failure"},
    {"pattern": "1B00", "label": "GET CURVE ERR", "detail": "get curve failure"},
    {"pattern": "1C00", "label": "ATOD INIT ERR", "detail": "A/D calib STBY transition not detected"},
    {"pattern": "1D00", "label": "RESULTS DATA ERR", "detail": "results data error"},
    {"pattern": "1E00", "label": "CLOCK ERR", "detail": "clock communications error"},
    {"pattern": "1F00", "label": "OVERLAP ERR", "detail": "bandpass overlap in filterset"},
    {"pattern": "2000", "label": "BARCODE ERR", "detail": "no valid barcode detected"},
    {"pattern": "2100", "label": "INVALID PARAM ERR", "detail": "invalid parameter value selected"},
    {"pattern": "220.", "label": "PMT ERR", "detail": "PMT test signal too high", "vars": [("test_type", 3)]},
    {"pattern": "23..", "label": "LAMP ERR", "detail": "lamp control failure", "vars": [("subcode", 2), ("test_type", 3)]},
    {"pattern": "240.", "label": "SENSOR POS ERR", "detail": "test sensor position incorrect", "vars": [("motor", 3)]},
    {"pattern": "2500", "label": "FLASH MISS ERR", "detail": "motor passed flash location too soon"},
    {"pattern": "2600", "label": "XY LIMIT ERR", "detail": "physical limit exceeded for area scan"},
    {"pattern": "270.", "label": "PANEL METHOD ERR", "detail": "method does not match first panel assay", "vars": [("assay", 3)]},
    {"pattern": "280.", "label": "MOTOR TIMER ERR", "detail": "motor timer not available", "vars": [("motor", 3)]},
    {"pattern": "A100", "label": "TCB NOT AVAIL ERR", "detail": "task control block not available"},
    {"pattern": "A200", "label": "READ NOT AVAIL ERR", "detail": "read already in progress"},
    {"pattern": "A30.", "label": "NOT AVAIL ERR", "detail": "device not available", "vars": [("device", 3)]},
    {"pattern": "A400", "label": "CHECKSUM ERR", "detail": "failed code checksum test"},
    {"pattern": "A50.", "label": "DR ALLOC ERR", "detail": "DR steps alloc/free error", "vars": [("assay", 3)]},
    {"pattern": "A600", "label": "DFLASH TIMEOUT ERR", "detail": "data flash write timed out"},
    {"pattern": "A7..", "label": "DFLASH ERR", "detail": "data flash readback did not match write", "vars": [("data_flash_test", 2), ("chip", 3)]},
    {"pattern": "A800", "label": "CFLASH TIMEOUT ERR", "detail": "code flash write timed out"},
    {"pattern": "A900", "label": "HEAP CORRUPTION ERR", "detail": "memory allocation heap corrupted"},
]


def _pattern_match(pattern: str, code: str) -> bool:
    if len(pattern) != len(code):
        return False
    for p, c in zip(pattern, code):
        if p != "." and p != c:
            return False
    return True


def _format_error_var(name: str, value: str) -> str:
    value = value.upper()
    if name == "test_type":
        desc = TEST_TYPE_CODES.get(value)
        return f"test type {value}" + (f": {desc}" if desc else "")
    if name == "motor":
        desc = MOTOR_CODES.get(value)
        return f"motor {value}" + (f": {desc}" if desc else "")
    if name == "incubator_code":
        desc = INCUBATOR_CODES.get(value)
        return f"incubator code {value}" + (f": {desc}" if desc else "")
    if name == "data_flash_test":
        desc = DATA_FLASH_CODES.get(value)
        return f"flash test {value}" + (f": {desc}" if desc else "")
    if name == "zones":
        return f"zones mask {value}"
    if name == "channel":
        return f"channel {value}"
    if name == "filter":
        return f"filter {value}"
    if name == "read_filter":
        return f"read filter {value}"
    if name == "assay":
        return f"assay {value}"
    if name == "device":
        return f"device {value}"
    if name == "chip":
        return f"chip {value}"
    if name == "subcode":
        return f"subcode {value}"
    return f"{name} {value}"


def _describe_312_status(code: str) -> str | None:
    if len(code) != 3:
        return None
    s2 = code[1].upper()
    desc = STATUS_312_CODES.get(s2)
    if not desc or s2 == "0":
        return None
    return f"312 status {s2}: {desc}"


def _describe_elx_status(code: str) -> str | None:
    if not code:
        return None
    code = code.upper()
    if code == "0000":
        return None
    for rule in ELX_ERROR_RULES:
        if not _pattern_match(rule["pattern"], code):
            continue
        label = rule["label"]
        detail = rule.get("detail")
        summary = f"{label}"
        if detail:
            summary = f"{summary}: {detail}"
        extras = []
        for name, idx in rule.get("vars", []):
            if 0 <= idx < len(code):
                extras.append(_format_error_var(name, code[idx]))
        if extras:
            summary = f"{summary} ({'; '.join(extras)})"
        return summary
    return f"ELx status {code}: unknown error"


def _describe_status(status: core.Status | None) -> str | None:
    if not status:
        return None
    if status.mode == "312":
        return _describe_312_status(status.code)
    if status.mode == "ELx":
        return _describe_elx_status(status.code)
    return None


def _recommendations_for_status(status: core.Status | None) -> list[str]:
    recs: list[str] = []

    def add(item: str) -> None:
        if item and item not in recs:
            recs.append(item)

    if not status:
        add("No status returned. Verify cabling and serial settings, then retry.")
        return recs

    code = status.code.upper() if status.code else ""
    if status.mode == "312":
        if len(code) >= 2 and code[1] == "0":
            add("No active errors detected.")
            return recs
        add("Check the reader display for the matching error code.")
        s2 = code[1] if len(code) >= 2 else ""
        if s2 == "8":
            add("Run a self-test (`*`) before retrying the read.")
            add("Power-cycle if the self-test fails or the error persists.")
        elif s2 in ("9", "A"):
            add("Review assay and well range selection, then resend the assay definition.")
            add("Retry after confirming the profile matches the plate layout.")
        elif s2 in ("B", "C"):
            add("Confirm incubator settings or disable incubation in the assay.")
            add("Power-cycle if the incubator error persists.")
        elif s2 == "E":
            add("Check barcode label and scanner alignment, or disable barcode reads.")
        return recs

    if status.mode != "ELx":
        add("Unknown status format. Retry the status check.")
        return recs

    if code == "0000":
        add("No active errors detected.")
        return recs

    add("Check the reader display for the matching error code.")
    if code.startswith("A"):
        add("Power-cycle the instrument to clear fatal errors.")
        add("If the error returns, service may be required.")
        return recs
    if code.startswith(("02", "03", "04", "13", "24", "25", "26")):
        add("Ensure the plate carrier path is clear and the plate is seated.")
        add("Run a self-test to re-home axes.")
    if code.startswith("0E"):
        add("Verify the requested wavelength filter is installed and matches the profile.")
    if code.startswith("15"):
        add("Confirm incubator settings or disable incubation in the assay definition.")
    if code.startswith("23"):
        add("Check lamp condition and allow warm-up, then run a self-test.")
    if code == "1600":
        add("Resend the assay definition and confirm profile settings.")
    if code == "1700":
        add("Increase the kinetic interval or reduce read options.")
    if code == "1800":
        add("Reduce kinetic interval count or simplify the read.")
    if code == "1C00":
        add("Run a self-test to recalibrate A/D.")
    if code == "1D00":
        add("Discard partial data from this read and rerun the assay.")
    if code == "1E00":
        add("Power-cycle the instrument to reset the clock subsystem.")
    if code == "1F00":
        add("Adjust filter selection to avoid bandpass overlap.")
    if code == "2000":
        add("Check barcode label orientation or disable barcode reads.")
    if code == "2100":
        add("Review parameter ranges in the assay definition.")
    if code.startswith("22"):
        add("Run a self-test and recheck detector settings.")
    return recs


class RunState:
    def __init__(
        self,
        run_id: str,
        cmd: list[str],
        paths: dict[str, str],
        mode: str,
        meta: dict[str, str],
    ):
        self.run_id = run_id
        self.cmd = cmd
        self.paths = paths
        self.mode = mode
        self.meta = meta
        self.db_id: int | None = None
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
            "mode": self.mode,
            "meta": self.meta,
            "db_id": self.db_id,
            "started_at": self.started_at.isoformat(),
            "ended_at": self.ended_at.isoformat() if self.ended_at else None,
            "returncode": self.returncode,
            "active": self.returncode is None and self.ended_at is None,
        }


RUNS: dict[str, RunState] = {}
RUNS_LOCK = threading.Lock()


def _init_db() -> None:
    global DB, DB_ERROR
    if elx808_db is None:
        DB_ERROR = "psycopg not installed"
        return
    db = elx808_db.Database.from_env()
    if db is None:
        DB_ERROR = "ELX808_DB_URL or DATABASE_URL not set"
        return
    try:
        db.ensure_schema()
        db.seed_demo_if_empty()
    except Exception as exc:
        DB_ERROR = f"database init failed: {exc}"
        return
    DB = db


def _db_ready() -> bool:
    return DB is not None


def _db_status() -> dict:
    if DB is not None:
        return {"available": True, "error": None}
    return {"available": False, "error": DB_ERROR}


def _db_call(func, *args, **kwargs):
    if DB is None:
        return None
    try:
        return func(*args, **kwargs)
    except Exception as exc:
        print(f"db error: {exc}")
        return None


def _probe_instrument_state(
    port: str,
    *,
    baud: int = 9600,
    databits: int = 8,
    parity: str = "N",
    stopbits: int = 2,
    flow: str = "none",
    timeout: float = 2.0,
) -> dict:
    if not port:
        return {
            "state": "disconnected",
            "error": "port required",
            "recommendations": ["Select a serial port before checking status."],
        }
    try:
        fd = os.open(port, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
    except OSError as exc:
        return {
            "state": "disconnected",
            "error": str(exc),
            "recommendations": ["Verify the serial adapter and permissions, then retry."],
        }
    try:
        sc.configure_serial(
            fd,
            baud=baud,
            databits=databits,
            parity=parity,
            stopbits=stopbits,
            flow=flow,
        )
        os.write(fd, b"o")
        raw = core.read_response(fd, overall_timeout=timeout, quiet_timeout=0.4)
        if not raw:
            return {
                "state": "no-response",
                "recommendations": ["No response received. Verify cabling and baud rate."],
            }
        parsed = core.parse_response(raw)
        status = parsed.status_parsed
        status_mode = status.mode if status else None
        status_code = status.code if status else None
        ok = status_code in ("0000", "000")
        status_description = _describe_status(status) if not ok else None
        recommendations = (
            ["No active errors detected."]
            if ok
            else _recommendations_for_status(status)
        )
        state = "idle" if ok else "attention"
        return {
            "state": state,
            "ack": parsed.ack,
            "nak": parsed.nak,
            "status_mode": status_mode,
            "status_code": status_code,
            "status_description": status_description,
            "recommendations": recommendations,
            "raw_hex": core.hexdump(parsed.raw),
        }
    finally:
        os.close(fd)


def _load_env_file(path: Path) -> None:
    if not path.exists():
        return
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if not key:
            continue
        if (value.startswith('"') and value.endswith('"')) or (
            value.startswith("'") and value.endswith("'")
        ):
            value = value[1:-1]
        os.environ.setdefault(key, value)


def _run_state_path(run_id: str) -> Path:
    return STATE_DIR / f"run-{run_id}.json"


def _load_run_state_file(path: Path) -> dict | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    if not isinstance(data, dict):
        return None
    return data


def _load_run_state(run_id: str) -> dict | None:
    path = _run_state_path(run_id)
    if not path.exists():
        return None
    return _load_run_state_file(path)


def _write_run_state(state: RunState) -> None:
    path = _run_state_path(state.run_id)
    tmp_path = path.with_suffix(".tmp")
    data = json.dumps(state.to_dict(), indent=2)
    tmp_path.write_text(data + "\n", encoding="utf-8")
    tmp_path.replace(path)


def _list_runs() -> list[dict]:
    runs: dict[str, dict] = {}
    for path in sorted(STATE_DIR.glob("run-*.json")):
        data = _load_run_state_file(path)
        if not data or "id" not in data:
            continue
        runs[str(data["id"])] = data
    with RUNS_LOCK:
        active_ids = {run_id for run_id, state in RUNS.items() if state.returncode is None}
        for run_id, state in RUNS.items():
            runs[run_id] = state.to_dict()
    for run_id, data in runs.items():
        is_active = run_id in active_ids
        data["active"] = is_active
        data["stale"] = (
            not is_active
            and data.get("returncode") is None
            and data.get("ended_at") is None
        )
    return sorted(runs.values(), key=lambda item: item.get("started_at", ""), reverse=True)


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
      button.danger {
        background: #f3c9bf;
        color: #6d1f10;
      }
      .run-list {
        display: grid;
        gap: 10px;
      }
      .run-item {
        border: 1px solid var(--line);
        border-radius: 12px;
        padding: 10px;
        background: #fffdf8;
      }
      .run-item strong {
        font-size: 13px;
      }
      .run-meta {
        margin-top: 4px;
        font-size: 12px;
        color: var(--muted);
      }
      .run-path {
        margin-top: 4px;
        font-size: 11px;
        color: var(--muted);
        word-break: break-all;
      }
      .run-actions {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 8px;
      }
      .run-actions button {
        padding: 6px 10px;
        font-size: 12px;
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
      .alert-box {
        border: 1px solid var(--line);
        border-radius: 12px;
        padding: 10px 12px;
        background: #fffdf8;
      }
      .alert-box.warning {
        background: rgba(232, 93, 63, 0.08);
        border-color: rgba(232, 93, 63, 0.25);
      }
      .alert-title {
        font-size: 13px;
        font-weight: 600;
        margin-bottom: 6px;
      }
      .alert-list {
        margin: 0;
        padding-left: 18px;
        font-size: 12px;
        color: var(--muted);
      }
      .alert-list li {
        margin-bottom: 4px;
      }
      .matrix-panel {
        margin-top: 16px;
        border-top: 1px solid var(--line);
        padding-top: 14px;
      }
      .matrix-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 10px;
        font-size: 12px;
      }
      .matrix-table th,
      .matrix-table td {
        border: 1px solid var(--line);
        padding: 6px 6px;
        text-align: right;
        background: #fffdf8;
      }
      .matrix-table th:first-child,
      .matrix-table td:first-child {
        text-align: center;
        background: #f7efe4;
        font-weight: 600;
      }
      .matrix-table th {
        background: #f0e5d6;
      }
      .kinetic-panel {
        margin-top: 18px;
        border-top: 1px dashed var(--line);
        padding-top: 16px;
      }
      .kinetic-scroll {
        overflow-x: auto;
        padding-bottom: 6px;
      }
      .kinetic-grid {
        display: grid;
        grid-template-columns: repeat(12, minmax(70px, 1fr));
        gap: 10px;
        min-width: 980px;
      }
      .kinetic-card {
        background:
          linear-gradient(140deg, rgba(255, 248, 240, 0.95) 0%, rgba(236, 248, 246, 0.95) 100%);
        border: 1px solid var(--line);
        border-radius: 14px;
        padding: 6px 6px 8px;
        box-shadow: 0 8px 16px rgba(36, 28, 22, 0.12);
        position: relative;
        min-height: 68px;
        animation: rise 0.5s ease both;
      }
      .kinetic-label {
        font-size: 10px;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: var(--muted);
        margin-bottom: 2px;
      }
      .sparkline {
        width: 100%;
        height: 42px;
        display: block;
      }
      .sparkline path {
        fill: none;
        stroke: var(--accent-2);
        stroke-width: 2.2;
        stroke-linecap: round;
        stroke-linejoin: round;
      }
      .sparkline .fill {
        fill: rgba(27, 143, 138, 0.15);
        stroke: none;
      }
      .sparkline .dot {
        fill: var(--accent);
        opacity: 0.8;
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
        <div class="field">
          <label>Instrument Status</label>
          <p class="pill" id="instrumentStatus">Unknown</p>
          <div id="instrumentDetails" class="run-meta"></div>
        </div>
        <div class="field">
          <label>Instrument Alerts</label>
          <div id="instrumentAlertBox" class="alert-box">
            <div id="instrumentAlertTitle" class="alert-title">No active errors detected.</div>
            <ul id="instrumentRecommendations" class="alert-list"></ul>
          </div>
        </div>
        <div class="buttons">
          <button class="primary" id="startBtn">Start Run</button>
          <button class="secondary" id="stopBtn" disabled>Stop</button>
          <button class="danger" id="shutdownBtn">Shutdown Web Interface</button>
          <button class="secondary" id="restartBtn">Restart Web Interface</button>
        </div>
        <div class="buttons">
          <button class="secondary" id="checkStatusBtn">Check Instrument</button>
        </div>
        <p class="pill" id="runBadge">Idle</p>
        <div class="field">
          <label>Recent Runs</label>
          <div id="runList" class="run-list">Loading...</div>
        </div>
        <div class="buttons">
          <button class="secondary" id="refreshRunsBtn">Refresh Runs</button>
        </div>
        <div class="field">
          <label>Database</label>
          <p class="pill" id="dbStatus">DB: checking...</p>
        </div>
        <div class="field">
          <label>Database Runs</label>
          <div id="dbRunList" class="run-list">Loading...</div>
        </div>
        <div class="buttons">
          <button class="secondary" id="refreshDbBtn">Refresh DB</button>
        </div>
      </section>
      <section class="panel">
        <div class="status">
          <span>Live Output</span>
          <span id="summary" class="badge">No run yet</span>
        </div>
        <pre id="output"></pre>
        <div class="matrix-panel">
          <div class="status">
            <span>Matrix View</span>
            <span id="matrixSummary" class="badge">No run selected</span>
          </div>
          <div class="row">
            <div class="field">
              <label for="matrixInterval">Interval</label>
              <select id="matrixInterval"></select>
            </div>
            <div class="field">
              <label for="matrixWavelength">Wavelength</label>
              <select id="matrixWavelength"></select>
            </div>
          </div>
          <div id="matrixTable"></div>
        </div>
        <div class="kinetic-panel">
          <div class="status">
            <span>Kinetic Grid</span>
            <span id="kineticSummary" class="badge">No run selected</span>
          </div>
          <div class="row">
            <div class="field">
              <label for="kineticWavelength">Wavelength</label>
              <select id="kineticWavelength"></select>
            </div>
            <div class="field">
              <label for="kineticRun">Run</label>
              <input id="kineticRun" placeholder="Select from Database Runs" disabled />
            </div>
          </div>
          <div class="kinetic-scroll">
            <div id="kineticGrid" class="kinetic-grid"></div>
          </div>
        </div>
      </section>
    </main>
    <script>
      const output = document.getElementById("output");
      const runBadge = document.getElementById("runBadge");
      const summary = document.getElementById("summary");
      const portInput = document.getElementById("port");
      const startBtn = document.getElementById("startBtn");
      const stopBtn = document.getElementById("stopBtn");
      const shutdownBtn = document.getElementById("shutdownBtn");
      const restartBtn = document.getElementById("restartBtn");
      const runList = document.getElementById("runList");
      const refreshRunsBtn = document.getElementById("refreshRunsBtn");
      const dbStatus = document.getElementById("dbStatus");
      const dbRunList = document.getElementById("dbRunList");
      const refreshDbBtn = document.getElementById("refreshDbBtn");
      const instrumentStatus = document.getElementById("instrumentStatus");
      const instrumentDetails = document.getElementById("instrumentDetails");
      const instrumentAlertBox = document.getElementById("instrumentAlertBox");
      const instrumentAlertTitle = document.getElementById("instrumentAlertTitle");
      const instrumentRecommendations = document.getElementById("instrumentRecommendations");
      const checkStatusBtn = document.getElementById("checkStatusBtn");
      const matrixSummary = document.getElementById("matrixSummary");
      const matrixInterval = document.getElementById("matrixInterval");
      const matrixWavelength = document.getElementById("matrixWavelength");
      const matrixTable = document.getElementById("matrixTable");
      const kineticSummary = document.getElementById("kineticSummary");
      const kineticWavelength = document.getElementById("kineticWavelength");
      const kineticRun = document.getElementById("kineticRun");
      const kineticGrid = document.getElementById("kineticGrid");
      const modeSelect = document.getElementById("mode");
      let currentRunId = null;
      let eventSource = null;
      let runsCache = [];
      let dbRunsCache = [];
      let matrixRunCode = null;
      let matrixSummaryCache = null;
      let kineticRunCode = null;
      let kineticSummaryCache = null;
      let instrumentState = "unknown";

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
        const storedPort = localStorage.getItem("elx808Port") || "";
        if (!portInput.value && storedPort) {
          portInput.value = storedPort;
        }
        try {
          const res = await fetch("/ports");
          const data = await res.json();
          const ports = data.ports || [];
          for (const port of data.ports) {
            const opt = document.createElement("option");
            opt.value = port;
            list.appendChild(opt);
          }
          if (!portInput.value) {
            if (storedPort && ports.includes(storedPort)) {
              portInput.value = storedPort;
            } else if (ports.length === 1) {
              portInput.value = ports[0];
              localStorage.setItem("elx808Port", ports[0]);
            }
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

      function updateActionAvailability() {
        if (currentRunId) {
          startBtn.disabled = true;
          stopBtn.disabled = false;
          return;
        }
        if (["disconnected", "busy", "no-response", "attention"].includes(instrumentState)) {
          startBtn.disabled = true;
          stopBtn.disabled = true;
          return;
        }
        startBtn.disabled = false;
        stopBtn.disabled = true;
      }

      function setInstrumentState(data) {
        instrumentState = data.state || "unknown";
        instrumentStatus.textContent = instrumentState.toUpperCase();
        instrumentStatus.className = "pill";
        if (instrumentState === "busy" || instrumentState === "attention") {
          instrumentStatus.classList.add("warning");
        }
        if (instrumentState === "disconnected" || instrumentState === "no-response") {
          instrumentStatus.classList.add("warning");
        }
        const details = [];
        if (data.status_mode && data.status_code) {
          details.push(`status ${data.status_mode}:${data.status_code}`);
        }
        if (data.status_description) {
          details.push(data.status_description);
        }
        if (data.run_id) {
          details.push(`run ${data.run_id}`);
        }
        if (data.error) {
          details.push(`error ${data.error}`);
        }
        instrumentDetails.textContent = details.join(" · ");
        instrumentAlertBox.classList.toggle(
          "warning",
          ["attention", "disconnected", "no-response"].includes(instrumentState)
        );
        instrumentRecommendations.innerHTML = "";
        const recs = Array.isArray(data.recommendations) ? data.recommendations : [];
        if (instrumentState === "attention") {
          instrumentAlertTitle.textContent = "Attention needed.";
        } else if (instrumentState === "idle") {
          instrumentAlertTitle.textContent = "No active errors detected.";
        } else if (instrumentState === "disconnected") {
          instrumentAlertTitle.textContent = "Instrument not connected.";
        } else if (instrumentState === "no-response") {
          instrumentAlertTitle.textContent = "No response from instrument.";
        } else {
          instrumentAlertTitle.textContent = "Instrument status unknown.";
        }
        const filteredRecs = recs.filter((rec) => {
          if (instrumentState !== "idle") return true;
          return !rec.toLowerCase().startsWith("no active errors");
        });
        for (const rec of filteredRecs) {
          const li = document.createElement("li");
          li.textContent = rec;
          instrumentRecommendations.appendChild(li);
        }
        updateActionAvailability();
      }

      function formatWhen(iso) {
        if (!iso) return "unknown time";
        const d = new Date(iso);
        if (Number.isNaN(d.getTime())) return iso;
        return d.toLocaleString();
      }

      function runStatus(run) {
        if (run.active) return { label: "Active", klass: "badge" };
        if (run.stale) return { label: "Stale", klass: "badge warning" };
        if (run.returncode && run.returncode !== 0) {
          return { label: `Error ${run.returncode}`, klass: "badge warning" };
        }
        return { label: "Complete", klass: "badge" };
      }

      function resetEventSource() {
        if (eventSource) {
          eventSource.close();
          eventSource = null;
        }
      }

      async function viewOutput(run) {
        resetEventSource();
        currentRunId = null;
        startBtn.disabled = false;
        stopBtn.disabled = true;
        output.textContent = "";
        try {
          const res = await fetch(`/runs/${run.id}/output`);
          if (!res.ok) {
            throw new Error("Output log not available");
          }
          output.textContent = await res.text();
          output.scrollTop = output.scrollHeight;
          setRunState("Viewing Log", `Run ${run.id}`);
        } catch (err) {
          setRunState("Error", err.message);
        }
      }

      function attachToRun(run) {
        if (!run.active) {
          viewOutput(run);
          return;
        }
        resetEventSource();
        output.textContent = "";
        currentRunId = run.id;
        startBtn.disabled = true;
        stopBtn.disabled = false;
        setInstrumentState({ state: "busy", run_id: run.id });
        setRunState("Running", `Run ${run.id}`);
        eventSource = new EventSource(`/events/${run.id}`);
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
          loadRuns({ autoAttach: false });
          loadDbRuns();
          if (msg.returncode) {
            checkInstrumentStatus({ silent: true });
          }
          updateActionAvailability();
        });
      }

      function renderRuns() {
        runList.innerHTML = "";
        if (!runsCache.length) {
          runList.textContent = "No runs yet.";
          return;
        }
        for (const run of runsCache.slice(0, 6)) {
          const item = document.createElement("div");
          item.className = "run-item";
          const status = runStatus(run);
          const title = document.createElement("div");
          title.innerHTML = `<strong>${run.id}</strong> <span class="${status.klass}">${status.label}</span>`;
          const meta = document.createElement("div");
          meta.className = "run-meta";
          meta.textContent = `${run.mode || "run"} · ${formatWhen(run.started_at)}`;
          const actions = document.createElement("div");
          actions.className = "run-actions";
          const attachBtn = document.createElement("button");
          attachBtn.className = "secondary";
          attachBtn.textContent = run.active ? "Attach" : "View Output";
          attachBtn.addEventListener("click", () => attachToRun(run));
          actions.appendChild(attachBtn);
          if (run.paths && run.paths.csv) {
            const csvBtn = document.createElement("button");
            csvBtn.className = "secondary";
            csvBtn.textContent = "Download CSV";
            csvBtn.addEventListener("click", () => {
              window.location.href = `/runs/${run.id}/csv`;
            });
            actions.appendChild(csvBtn);
          }
          if (run.paths && run.paths.manifest) {
            const manifestBtn = document.createElement("button");
            manifestBtn.className = "secondary";
            manifestBtn.textContent = "Manifest";
            manifestBtn.addEventListener("click", () => {
              window.location.href = `/runs/${run.id}/manifest`;
            });
            actions.appendChild(manifestBtn);
          }
          const paths = document.createElement("div");
          paths.className = "run-path";
          paths.textContent = run.paths && run.paths.csv ? `csv: ${run.paths.csv}` : "csv: -";
          item.appendChild(title);
          item.appendChild(meta);
          item.appendChild(actions);
          item.appendChild(paths);
          runList.appendChild(item);
        }
      }

      function dbStatusBadge(status) {
        if (!status) return { label: "unknown", klass: "badge warning" };
        if (status === "stored") return { label: "Stored", klass: "badge" };
        if (status === "running") return { label: "Running", klass: "badge" };
        if (status === "demo") return { label: "Demo", klass: "badge" };
        if (status === "error") return { label: "Error", klass: "badge warning" };
        return { label: status, klass: "badge" };
      }

      function renderDbRuns() {
        dbRunList.innerHTML = "";
        if (!dbRunsCache.length) {
          dbRunList.textContent = "No database runs yet.";
          return;
        }
        for (const run of dbRunsCache.slice(0, 6)) {
          const item = document.createElement("div");
          item.className = "run-item";
          const status = dbStatusBadge(run.status);
          const title = document.createElement("div");
          title.innerHTML = `<strong>${run.run_code}</strong> <span class="${status.klass}">${status.label}</span>`;
          const meta = document.createElement("div");
          meta.className = "run-meta";
          const sample = run.sample_label ? ` · ${run.sample_label} (pH ${run.sample_ph || "?"})` : "";
          meta.textContent = `${run.mode || "run"} · ${run.profile || "unknown"} · ${formatWhen(run.started_at)}${sample}`;
          const actions = document.createElement("div");
          actions.className = "run-actions";
          const csvBtn = document.createElement("button");
          csvBtn.className = "secondary";
          csvBtn.textContent = "Download CSV";
          csvBtn.addEventListener("click", () => {
            window.location.href = `/db/runs/${run.run_code}/csv`;
          });
          actions.appendChild(csvBtn);
          const deleteBtn = document.createElement("button");
          deleteBtn.className = "danger";
          deleteBtn.textContent = "Delete";
          deleteBtn.addEventListener("click", async () => {
            if (!confirm(`Delete run ${run.run_code} from the database?`)) return;
            await fetch(`/db/runs/${run.run_code}`, { method: "DELETE" });
            loadDbRuns();
          });
          actions.appendChild(deleteBtn);
          const viewBtn = document.createElement("button");
          viewBtn.className = "secondary";
          viewBtn.textContent = "View Matrix";
          viewBtn.addEventListener("click", () => {
            loadMatrixSummary(run.run_code);
          });
          actions.appendChild(viewBtn);
          const kineticsBtn = document.createElement("button");
          kineticsBtn.className = "secondary";
          kineticsBtn.textContent = "View Kinetics";
          kineticsBtn.addEventListener("click", () => {
            loadKineticSummary(run.run_code);
          });
          actions.appendChild(kineticsBtn);
          const paths = document.createElement("div");
          paths.className = "run-path";
          paths.textContent = `rows: ${run.reading_count || 0}`;
          item.appendChild(title);
          item.appendChild(meta);
          item.appendChild(actions);
          item.appendChild(paths);
          dbRunList.appendChild(item);
        }
      }

      async function loadDbStatus() {
        try {
          const res = await fetch("/db/status");
          const data = await res.json();
          if (data.available) {
            dbStatus.textContent = "DB: connected";
          } else {
            dbStatus.textContent = `DB: ${data.error || "unavailable"}`;
          }
        } catch (err) {
          dbStatus.textContent = "DB: unavailable";
        }
      }

      async function loadDbRuns() {
        try {
          const res = await fetch("/db/runs");
          if (!res.ok) {
            dbRunList.textContent = "Database unavailable.";
            return;
          }
          const data = await res.json();
          dbRunsCache = data.runs || [];
          renderDbRuns();
        } catch (err) {
          dbRunList.textContent = "Database unavailable.";
        }
      }

      function populateSelect(select, values, formatter) {
        select.innerHTML = "";
        for (const value of values) {
          const opt = document.createElement("option");
          opt.value = value;
          opt.textContent = formatter ? formatter(value) : value;
          select.appendChild(opt);
        }
      }

      async function loadMatrixSummary(runCode) {
        if (!runCode) return;
        matrixSummary.textContent = "Loading...";
        matrixRunCode = runCode;
        matrixSummaryCache = null;
        try {
          const res = await fetch(`/db/runs/${runCode}/summary`);
          if (!res.ok) {
            throw new Error("summary unavailable");
          }
          const data = await res.json();
          matrixSummaryCache = data;
          const intervals = data.intervals || [];
          const wavelengthsNm = data.wavelengths_nm || [];
          const wavelengthsIdx = data.wavelengths_index || [];
          if (intervals.length) {
            populateSelect(matrixInterval, intervals, (v) => `#${v}`);
          }
          if (wavelengthsNm.length) {
            populateSelect(matrixWavelength, wavelengthsNm, (v) => `${v} nm`);
            matrixWavelength.dataset.mode = "nm";
          } else if (wavelengthsIdx.length) {
            populateSelect(matrixWavelength, wavelengthsIdx, (v) => `Index ${v}`);
            matrixWavelength.dataset.mode = "index";
          } else {
            matrixWavelength.innerHTML = "";
          }
          matrixSummary.textContent = `Run ${runCode}`;
          loadMatrix();
        } catch (err) {
          matrixSummary.textContent = "Matrix unavailable";
        }
      }

      async function loadMatrix() {
        if (!matrixRunCode) return;
        const interval = matrixInterval.value || "1";
        const wavelength = matrixWavelength.value || "";
        const mode = matrixWavelength.dataset.mode;
        let url = `/db/runs/${matrixRunCode}/matrix?interval=${encodeURIComponent(interval)}`;
        if (wavelength) {
          if (mode === "index") {
            url += `&wavelength_index=${encodeURIComponent(wavelength)}`;
          } else {
            url += `&wavelength_nm=${encodeURIComponent(wavelength)}`;
          }
        }
        try {
          const res = await fetch(url);
          if (!res.ok) {
            throw new Error("matrix unavailable");
          }
          const data = await res.json();
          renderMatrix(data);
        } catch (err) {
          matrixTable.textContent = "Matrix unavailable.";
        }
      }

      function renderMatrix(data) {
        const rows = data.rows || 0;
        const cols = data.cols || 0;
        if (!rows || !cols) {
          matrixTable.textContent = "No matrix data.";
          return;
        }
        const lookup = new Map();
        for (const cell of data.cells || []) {
          lookup.set(`${cell.row}-${cell.col}`, cell);
        }
        const table = document.createElement("table");
        table.className = "matrix-table";
        const thead = document.createElement("thead");
        const headerRow = document.createElement("tr");
        const corner = document.createElement("th");
        corner.textContent = "";
        headerRow.appendChild(corner);
        for (let c = 1; c <= cols; c += 1) {
          const th = document.createElement("th");
          th.textContent = c;
          headerRow.appendChild(th);
        }
        thead.appendChild(headerRow);
        table.appendChild(thead);
        const tbody = document.createElement("tbody");
        for (let r = 1; r <= rows; r += 1) {
          const tr = document.createElement("tr");
          const rowHead = document.createElement("th");
          rowHead.textContent = String.fromCharCode(64 + r);
          tr.appendChild(rowHead);
          for (let c = 1; c <= cols; c += 1) {
            const td = document.createElement("td");
            const cell = lookup.get(`${r}-${c}`);
            if (cell && cell.value !== null && cell.value !== undefined) {
              td.textContent = Number(cell.value).toFixed(3);
            } else {
              td.textContent = "";
            }
            tr.appendChild(td);
          }
          tbody.appendChild(tr);
        }
        table.appendChild(tbody);
        matrixTable.innerHTML = "";
        matrixTable.appendChild(table);
        const wavelengthLabel = data.wavelength_nm || data.wavelength_index || "";
        matrixSummary.textContent = `Run ${data.run_code} · Interval ${data.interval} · ${wavelengthLabel}`;
      }

      async function loadKineticSummary(runCode) {
        if (!runCode) return;
        kineticSummary.textContent = "Loading...";
        kineticRun.value = runCode;
        kineticRunCode = runCode;
        kineticSummaryCache = null;
        try {
          const res = await fetch(`/db/runs/${runCode}/summary`);
          if (!res.ok) {
            throw new Error("summary unavailable");
          }
          const data = await res.json();
          kineticSummaryCache = data;
          const wavelengthsNm = data.wavelengths_nm || [];
          const wavelengthsIdx = data.wavelengths_index || [];
          if (wavelengthsNm.length) {
            populateSelect(kineticWavelength, wavelengthsNm, (v) => `${v} nm`);
            kineticWavelength.dataset.mode = "nm";
          } else if (wavelengthsIdx.length) {
            populateSelect(kineticWavelength, wavelengthsIdx, (v) => `Index ${v}`);
            kineticWavelength.dataset.mode = "index";
          } else {
            kineticWavelength.innerHTML = "";
          }
          kineticSummary.textContent = `Run ${runCode}`;
          loadKineticGrid();
        } catch (err) {
          kineticSummary.textContent = "Kinetics unavailable";
        }
      }

      async function loadKineticGrid() {
        if (!kineticRunCode) return;
        const wavelength = kineticWavelength.value || "";
        const mode = kineticWavelength.dataset.mode;
        let url = `/db/runs/${kineticRunCode}/kinetics`;
        if (wavelength) {
          if (mode === "index") {
            url += `?wavelength_index=${encodeURIComponent(wavelength)}`;
          } else {
            url += `?wavelength_nm=${encodeURIComponent(wavelength)}`;
          }
        }
        try {
          const res = await fetch(url);
          if (!res.ok) {
            throw new Error("kinetics unavailable");
          }
          const data = await res.json();
          renderKineticGrid(data);
        } catch (err) {
          kineticGrid.textContent = "Kinetic grid unavailable.";
        }
      }

      function clamp01(value) {
        if (value === null || value === undefined || Number.isNaN(value)) return null;
        return Math.max(0, Math.min(1, Number(value)));
      }

      function buildSparkline(values) {
        const width = 96;
        const height = 42;
        const pad = 4;
        const points = [];
        const clamped = values.map((value) => clamp01(value));
        const count = clamped.length;
        if (!count) return "";
        const step = count > 1 ? (width - pad * 2) / (count - 1) : 0;
        for (let i = 0; i < count; i += 1) {
          const v = clamped[i];
          if (v === null) {
            points.push(null);
            continue;
          }
          const x = pad + step * i;
          const y = height - pad - v * (height - pad * 2);
          points.push([x, y]);
        }
        const segments = points.filter((pt) => pt);
        if (!segments.length) return "";
        const line = segments
          .map((pt, idx) => `${idx === 0 ? "M" : "L"} ${pt[0].toFixed(1)} ${pt[1].toFixed(1)}`)
          .join(" ");
        const last = segments[segments.length - 1];
        const fill = `${line} L ${last[0].toFixed(1)} ${height - pad} L ${segments[0][0].toFixed(1)} ${height - pad} Z`;
        return `
          <svg class="sparkline" viewBox="0 0 ${width} ${height}" preserveAspectRatio="none">
            <path class="fill" d="${fill}"></path>
            <path d="${line}"></path>
            <circle class="dot" cx="${last[0].toFixed(1)}" cy="${last[1].toFixed(1)}" r="2.4"></circle>
          </svg>
        `;
      }

      function renderKineticGrid(data) {
        const wells = data.wells || [];
        kineticGrid.innerHTML = "";
        if (!wells.length) {
          kineticGrid.textContent = "No kinetic data.";
          return;
        }
        for (const well of wells) {
          const card = document.createElement("div");
          card.className = "kinetic-card";
          const label = document.createElement("div");
          label.className = "kinetic-label";
          label.textContent = well.well;
          card.appendChild(label);
          const sparkWrap = document.createElement("div");
          sparkWrap.innerHTML = buildSparkline(well.values || []);
          card.appendChild(sparkWrap);
          kineticGrid.appendChild(card);
        }
        if (data.wavelength_nm) {
          kineticSummary.textContent = `Run ${data.run_code} · ${data.wavelength_nm} nm`;
        } else if (data.wavelength_index) {
          kineticSummary.textContent = `Run ${data.run_code} · Index ${data.wavelength_index}`;
        } else {
          kineticSummary.textContent = `Run ${data.run_code}`;
        }
      }

      async function loadRuns({ autoAttach = true } = {}) {
        try {
          const res = await fetch("/runs");
          if (!res.ok) {
            throw new Error("runs unavailable");
          }
          const data = await res.json();
          runsCache = data.runs || [];
          renderRuns();
          if (autoAttach && !currentRunId) {
            const active = runsCache.find((run) => run.active);
            if (active) {
              attachToRun(active);
            }
          }
        } catch (err) {
          runList.textContent = "Runs unavailable.";
        }
      }

      modeSelect.addEventListener("change", () => {
        updateProfileDefaults();
        setDefaults();
      });

      portInput.addEventListener("change", () => {
        const value = portInput.value.trim();
        if (value) {
          localStorage.setItem("elx808Port", value);
        }
      });

      refreshRunsBtn.addEventListener("click", () => {
        loadRuns({ autoAttach: false });
      });

      refreshDbBtn.addEventListener("click", () => {
        loadDbStatus();
        loadDbRuns();
      });

      async function checkInstrumentStatus({ silent = false } = {}) {
        const port = document.getElementById("port").value.trim();
        if (!port) {
          if (!silent) {
            alert("Serial port is required to check status.");
          }
          return;
        }
        instrumentStatus.textContent = "CHECKING...";
        instrumentDetails.textContent = "";
        try {
          const res = await fetch(`/instrument/state?port=${encodeURIComponent(port)}`);
          const data = await res.json();
          setInstrumentState(data);
        } catch (err) {
          setInstrumentState({ state: "disconnected", error: err.message });
        }
      }

      checkStatusBtn.addEventListener("click", async () => {
        await checkInstrumentStatus();
      });

      matrixInterval.addEventListener("change", () => {
        loadMatrix();
      });

      matrixWavelength.addEventListener("change", () => {
        loadMatrix();
      });

      kineticWavelength.addEventListener("change", () => {
        loadKineticGrid();
      });

      startBtn.addEventListener("click", async () => {
        if (!document.getElementById("confirm").checked) {
          alert("Please confirm instrument control before starting.");
          return;
        }
        if (["busy", "disconnected", "no-response", "attention"].includes(instrumentState)) {
          alert("Instrument is not ready. Check status before starting.");
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
          setInstrumentState({ state: "busy", run_id: data.id });
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
            loadRuns({ autoAttach: false });
            loadDbRuns();
            updateActionAvailability();
          });
          loadRuns({ autoAttach: false });
        } catch (err) {
          setRunState("Error", err.message);
          startBtn.disabled = false;
          stopBtn.disabled = true;
          currentRunId = null;
          updateActionAvailability();
        }
      });

      stopBtn.addEventListener("click", async () => {
        if (!currentRunId) return;
        await fetch(`/stop/${currentRunId}`, { method: "POST" });
        setRunState("Stopping...", "Sending terminate");
      });

      shutdownBtn.addEventListener("click", async () => {
        if (currentRunId) {
          alert("A run is active. Stop it before shutting down the server.");
          return;
        }
        if (!confirm("Shutdown the web UI server?")) return;
        setRunState("Shutting down...", "Server exiting");
        startBtn.disabled = true;
        stopBtn.disabled = true;
        shutdownBtn.disabled = true;
        try {
          await fetch("/shutdown", { method: "POST" });
        } catch (err) {
          console.warn("shutdown request failed", err);
        }
      });

      restartBtn.addEventListener("click", async () => {
        if (currentRunId) {
          alert("A run is active. Stop it before restarting the server.");
          return;
        }
        if (!confirm("Restart the web interface now?")) return;
        setRunState("Restarting...", "Server restarting");
        startBtn.disabled = true;
        stopBtn.disabled = true;
        shutdownBtn.disabled = true;
        restartBtn.disabled = true;
        try {
          await fetch("/restart", { method: "POST" });
        } catch (err) {
          console.warn("restart request failed", err);
        }
      });

      setDefaults();
      updateProfileDefaults();
      loadPorts();
      loadRuns();
      loadDbStatus();
      loadDbRuns();
      updateActionAvailability();
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
        "ui_log": f"{base}.ui.log",
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
    ui_log_path = state.paths.get("ui_log", "")
    ui_log = open(ui_log_path, "a", encoding="utf-8") if ui_log_path else None
    try:
        for line in process.stdout:
            clean = line.rstrip("\n")
            state.lines.append(clean)
            state.queue.put(clean)
            if ui_log:
                ui_log.write(clean + "\n")
                ui_log.flush()
        process.wait()
        state.returncode = process.returncode
        state.ended_at = _dt.datetime.now()
        state.queue.put(None)
    finally:
        if ui_log:
            ui_log.close()
    _write_run_state(state)
    if _db_ready():
        manifest_data = None
        manifest_path = state.paths.get("manifest")
        if manifest_path:
            try:
                manifest_data = json.loads(Path(manifest_path).read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                manifest_data = None
        status = "error" if state.returncode else "complete"
        meta = {"manifest": manifest_data} if manifest_data else {}
        _db_call(
            DB.record_run_end,
            run_code=state.run_id,
            ended_at=state.ended_at,
            returncode=state.returncode,
            status=status,
            meta=meta,
        )
        csv_path = state.paths.get("csv")
        if status == "complete" and csv_path and Path(csv_path).exists():
            inserted = _db_call(DB.replace_readings_from_csv, state.run_id, csv_path)
            if inserted is not None:
                _db_call(DB.mark_run_stored, state.run_id)


def _get_run_state(run_id: str) -> dict | None:
    with RUNS_LOCK:
        state = RUNS.get(run_id)
    if state:
        return state.to_dict()
    data = _load_run_state(run_id)
    if not data:
        return None
    data["active"] = False
    data["stale"] = data.get("returncode") is None and data.get("ended_at") is None
    return data


def _send_run_file(handler: BaseHTTPRequestHandler, run_id: str, key: str) -> None:
    data = _get_run_state(run_id)
    if not data:
        _error(handler, "run not found", 404)
        return
    paths = data.get("paths") or {}
    path = paths.get(key)
    if not path:
        _error(handler, "file not available", 404)
        return
    file_path = Path(path)
    if not file_path.exists():
        _error(handler, "file not found", 404)
        return
    content_type = "text/plain"
    if key == "csv":
        content_type = "text/csv"
    elif key == "manifest":
        content_type = "application/json"
    payload = file_path.read_bytes()
    handler.send_response(HTTPStatus.OK)
    handler.send_header("Content-Type", content_type)
    handler.send_header("Content-Length", str(len(payload)))
    handler.send_header(
        "Content-Disposition",
        f"attachment; filename={file_path.name}",
    )
    handler.end_headers()
    handler.wfile.write(payload)


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
        if parsed.path == "/db/status":
            _json_response(self, _db_status())
            return
        if parsed.path == "/db/runs":
            if not _db_ready():
                _error(self, "database unavailable", 503)
                return
            runs = _db_call(DB.list_runs) or []
            _json_response(self, {"runs": [run.__dict__ for run in runs]})
            return
        if parsed.path == "/instrument/state":
            params = urllib.parse.parse_qs(parsed.query or "")
            port = params.get("port", [""])[0]
            with RUNS_LOCK:
                active = next(
                    (state for state in RUNS.values() if state.process and state.returncode is None),
                    None,
                )
            if active:
                _json_response(
                    self,
                    {
                        "state": "busy",
                        "run_id": active.run_id,
                        "mode": active.mode,
                    },
                )
                return
            result = _probe_instrument_state(port)
            _json_response(self, result)
            return
        if parsed.path.startswith("/db/runs/"):
            if not _db_ready():
                _error(self, "database unavailable", 503)
                return
            parts = parsed.path.strip("/").split("/")
            if len(parts) >= 4 and parts[0] == "db" and parts[1] == "runs":
                run_code = urllib.parse.unquote(parts[2])
                action = parts[3]
                if action == "csv":
                    csv_text = _db_call(DB.export_run_csv, run_code)
                    if not csv_text:
                        _error(self, "run not found", 404)
                        return
                    payload = csv_text.encode("utf-8")
                    self.send_response(HTTPStatus.OK)
                    self.send_header("Content-Type", "text/csv")
                    self.send_header("Content-Length", str(len(payload)))
                    self.send_header(
                        "Content-Disposition",
                        f"attachment; filename={run_code}.csv",
                    )
                    self.end_headers()
                    self.wfile.write(payload)
                    return
                if action == "summary":
                    summary = _db_call(DB.get_run_summary, run_code)
                    if not summary:
                        _error(self, "run not found", 404)
                        return
                    _json_response(self, summary)
                    return
                if action == "matrix":
                    params = urllib.parse.parse_qs(parsed.query or "")
                    interval = int(params.get("interval", ["1"])[0])
                    wavelength_nm = params.get("wavelength_nm", [None])[0]
                    wavelength_index = params.get("wavelength_index", [None])[0]
                    wl_nm_val = int(wavelength_nm) if wavelength_nm else None
                    wl_idx_val = int(wavelength_index) if wavelength_index else None
                    matrix = _db_call(
                        DB.get_matrix,
                        run_code,
                        interval=interval,
                        wavelength_nm=wl_nm_val,
                        wavelength_index=wl_idx_val,
                    )
                    if not matrix:
                        _error(self, "run not found", 404)
                        return
                    _json_response(self, matrix)
                    return
                if action == "kinetics":
                    params = urllib.parse.parse_qs(parsed.query or "")
                    wavelength_nm = params.get("wavelength_nm", [None])[0]
                    wavelength_index = params.get("wavelength_index", [None])[0]
                    wl_nm_val = int(wavelength_nm) if wavelength_nm else None
                    wl_idx_val = int(wavelength_index) if wavelength_index else None
                    kinetics = _db_call(
                        DB.get_kinetic_series,
                        run_code,
                        wavelength_nm=wl_nm_val,
                        wavelength_index=wl_idx_val,
                    )
                    if not kinetics:
                        _error(self, "run not found", 404)
                        return
                    _json_response(self, kinetics)
                    return
        if parsed.path == "/runs":
            _json_response(self, {"runs": _list_runs()})
            return
        if parsed.path.startswith("/runs/"):
            parts = parsed.path.strip("/").split("/")
            if len(parts) == 2:
                run_id = parts[1]
                data = _get_run_state(run_id)
                if not data:
                    _error(self, "run not found", 404)
                    return
                _json_response(self, data)
                return
            if len(parts) == 3:
                run_id, kind = parts[1], parts[2]
                if kind in ("output", "log", "csv", "manifest", "ui_log"):
                    key = "ui_log" if kind == "output" else kind
                    _send_run_file(self, run_id, key)
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
        if parsed.path == "/restart":
            with RUNS_LOCK:
                active = any(state.process and state.returncode is None for state in RUNS.values())
            if active:
                _error(self, "run active; stop it before restart", 409)
                return
            _json_response(self, {"status": "restarting"})

            def _restart_server() -> None:
                args = [sys.executable, str(Path(__file__).resolve())]
                os.execv(sys.executable, args)

            threading.Timer(0.2, _restart_server).start()
            return
        if parsed.path == "/shutdown":
            with RUNS_LOCK:
                active = any(state.process and state.returncode is None for state in RUNS.values())
            if active:
                _error(self, "run active; stop it before shutdown", 409)
                return
            _json_response(self, {"status": "shutting down"})

            def _shutdown_server() -> None:
                self.server.shutdown()

            threading.Thread(target=_shutdown_server, daemon=True).start()
            return
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
        run_id = _dt.datetime.now().strftime("%Y%m%d-%H%M%S")
        payload["id"] = run_id
        try:
            cmd, paths = _build_command(payload)
        except ValueError as exc:
            _error(self, str(exc), 400)
            return
        mode = payload.get("mode", "validate-short-run")
        meta = {
            "port": payload.get("port"),
            "profile": payload.get("profile"),
            "restore_profile": payload.get("restoreProfile"),
            "timeout": payload.get("timeout"),
            "quiet": payload.get("quiet"),
            "strict_complete": bool(payload.get("strictComplete")),
            "no_restore": bool(payload.get("noRestore")),
        }
        state = RunState(run_id, cmd, paths, mode, meta)
        with RUNS_LOCK:
            RUNS[run_id] = state
        _write_run_state(state)
        if _db_ready():
            db_id = _db_call(
                DB.record_run_start,
                run_code=run_id,
                mode=mode,
                profile=payload.get("profile"),
                port=payload.get("port"),
                started_at=state.started_at,
                paths=paths,
                meta=meta,
            )
            state.db_id = db_id
            _write_run_state(state)
        thread = threading.Thread(target=_run_worker, args=(state,), daemon=True)
        thread.start()
        _json_response(self, {"id": run_id, "paths": paths})

    def do_DELETE(self) -> None:
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path.startswith("/db/runs/"):
            if not _db_ready():
                _error(self, "database unavailable", 503)
                return
            parts = parsed.path.strip("/").split("/")
            if len(parts) != 3 or parts[0] != "db" or parts[1] != "runs":
                _error(self, "not found", 404)
                return
            run_code = urllib.parse.unquote(parts[2])
            deleted = _db_call(DB.delete_run, run_code)
            if not deleted:
                _error(self, "run not found", 404)
                return
            _json_response(self, {"deleted": run_code})
            return
        _error(self, "not found", 404)


def main() -> int:
    _load_env_file(ENV_PATH)
    _init_db()
    host = "127.0.0.1"
    port = 8088
    server = ThreadingHTTPServer((host, port), Handler)
    print(f"ELx808 web UI running at http://{host}:{port}")
    print("Press Ctrl-C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
