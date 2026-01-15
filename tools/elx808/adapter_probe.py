#!/usr/bin/env python3
"""
Best-effort USB-serial adapter probe.

This script cannot reliably determine electrical levels (RS-232 vs TTL).
It only inspects USB descriptor strings and known chipset hints. Always
confirm via adapter labeling or measurement before connecting to the ELx808.
"""

from __future__ import annotations

import argparse
import glob
import shutil
import subprocess
import sys
import time


RS232_HINTS = (
    "rs-232",
    "rs232",
    "rs 232",
    "rs-422",
    "rs422",
    "rs-485",
    "rs485",
)

TTL_HINTS = (
    "ttl",
    "uart",
    "usb-serial controller",
    "usb-serial",
    "usb uart",
    "ft232",
    "ftdi",
    "ch340",
    "ch341",
    "cp210",
    "silicon labs",
    "prolific",
    "pl2303",
    "wch",
    "qinheng",
)


def run_cmd(cmd: list[str]) -> str:
    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        return ""
    return result.stdout.strip()


def list_serial_nodes() -> list[str]:
    patterns: list[str]
    if sys.platform.startswith("darwin"):
        patterns = ["/dev/cu.*", "/dev/tty.*"]
    else:
        patterns = ["/dev/ttyUSB*", "/dev/ttyACM*", "/dev/tty.*"]
    nodes: set[str] = set()
    for pattern in patterns:
        for path in glob.glob(pattern):
            nodes.add(path)
    return sorted(nodes)


def classify_hint(text: str) -> str:
    lowered = text.lower()
    if any(h in lowered for h in RS232_HINTS):
        return "likely RS-232/line-level (still confirm)"
    if any(h in lowered for h in TTL_HINTS):
        return "commonly TTL-level USB-UART (confirm; may still be RS-232)"
    return "unknown/ambiguous; confirm by label or measurement"


def parse_system_profiler() -> list[dict[str, str]]:
    if not shutil.which("system_profiler"):
        return []
    output = run_cmd(["system_profiler", "SPUSBDataType", "-detailLevel", "mini"])
    if not output:
        return []
    devices: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    for line in output.splitlines():
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip())
        if line.rstrip().endswith(":"):
            # Skip bus headers (usually low indent); treat deeper entries as devices.
            if indent <= 4:
                if current:
                    devices.append(current)
                    current = None
                continue
            if current:
                devices.append(current)
            current = {"name": line.strip().rstrip(":")}
            continue
        if current and ":" in line:
            key, value = line.strip().split(":", 1)
            current[key.strip()] = value.strip()
    if current:
        devices.append(current)
    return devices


def parse_lsusb() -> list[dict[str, str]]:
    if not shutil.which("lsusb"):
        return []
    output = run_cmd(["lsusb"])
    if not output:
        return []
    devices: list[dict[str, str]] = []
    for line in output.splitlines():
        line = line.strip()
        if not line:
            continue
        devices.append({"name": line})
    return devices


def print_usb_hints() -> None:
    devices: list[dict[str, str]]
    if sys.platform.startswith("darwin"):
        devices = parse_system_profiler()
    else:
        devices = parse_lsusb()

    if not devices:
        print("USB devices: (no USB descriptor data available)")
        return

    print("USB devices (descriptor hints):")
    for dev in devices:
        summary = " | ".join(f"{k}: {v}" for k, v in dev.items())
        hint = classify_hint(summary)
        print(f"- {summary}")
        print(f"  hint: {hint}")


def watch_for_new_devices(duration: float, interval: float) -> None:
    baseline = set(list_serial_nodes())
    print("Baseline serial nodes:")
    for node in sorted(baseline):
        print(f"- {node}")
    print("Watching for new serial nodes...")
    deadline = time.time() + duration
    while time.time() < deadline:
        time.sleep(interval)
        current = set(list_serial_nodes())
        new_nodes = sorted(current - baseline)
        if new_nodes:
            print("New serial nodes detected:")
            for node in new_nodes:
                print(f"- {node}")
            return
    print("No new serial nodes detected in watch window.")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Best-effort USB-serial adapter probe (non-invasive)."
    )
    parser.add_argument(
        "--watch",
        type=float,
        default=0.0,
        help="Watch for new serial nodes for N seconds.",
    )
    parser.add_argument(
        "--interval",
        type=float,
        default=0.5,
        help="Polling interval in seconds when --watch is used.",
    )
    args = parser.parse_args()

    if args.watch > 0:
        watch_for_new_devices(args.watch, args.interval)

    nodes = list_serial_nodes()
    print("Detected serial nodes:")
    if nodes:
        for node in nodes:
            print(f"- {node}")
    else:
        print("- (none)")

    print_usb_hints()

    print(
        "Note: Electrical level (RS-232 vs TTL) cannot be verified in software. "
        "Confirm the adapter labeling or measure idle TX voltage before use."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
