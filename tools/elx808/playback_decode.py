#!/usr/bin/env python3
"""
Decode a captured ELx808 response log into CSV without hardware.
"""

from __future__ import annotations

import argparse
import re
import sys

import elx808_core as core
import control_stack as stack


def _hex_to_bytes(text: str) -> bytes:
    parts = [part for part in text.strip().split() if part]
    return bytes(int(part, 16) for part in parts)


def _parse_control_stack_log(path: str, *, label: str) -> bytes:
    pattern = re.compile(r"^(?P<label>\S+)\s+raw_hex=(?P<hex>[0-9a-fA-F ]+)")
    last = b""
    with open(path, "r", encoding="utf-8") as handle:
        for line in handle:
            match = pattern.match(line.strip())
            if not match:
                continue
            if match.group("label") != label:
                continue
            last = _hex_to_bytes(match.group("hex"))
    return last


def _parse_serial_capture_log(path: str) -> bytes:
    with open(path, "r", encoding="utf-8") as handle:
        lines = handle.readlines()
    last_tx = -1
    for idx, line in enumerate(lines):
        if line.startswith("tx "):
            last_tx = idx
    raw = bytearray()
    for line in lines[last_tx + 1 :]:
        if not line.startswith("rx "):
            continue
        if "hex=" not in line:
            continue
        after = line.split("hex=", 1)[1]
        hex_text = after.split(" ascii=", 1)[0].strip()
        if not hex_text:
            continue
        raw.extend(_hex_to_bytes(hex_text))
    return bytes(raw)


def _detect_format(path: str) -> str:
    with open(path, "r", encoding="utf-8") as handle:
        for line in handle:
            if " raw_hex=" in line:
                return "control-stack"
            if line.startswith("rx ") and "hex=" in line:
                return "serial-capture"
    return "unknown"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Decode a captured ELx808 log into CSV (no hardware)."
    )
    parser.add_argument("--log", required=True, help="Path to the capture/log file.")
    parser.add_argument(
        "--format",
        choices=["auto", "control-stack", "serial-capture"],
        default="auto",
        help="Log format (auto-detect by default).",
    )
    parser.add_argument(
        "--label",
        default="read-plate",
        help="control-stack label to decode (default: read-plate).",
    )
    parser.add_argument(
        "--wavelengths-per-interval",
        type=int,
        default=1,
        help="Number of wavelengths per kinetic interval (for grouping).",
    )
    parser.add_argument("--rows", type=int, default=8, help="Rows to decode (default 8).")
    parser.add_argument("--cols", type=int, default=12, help="Columns to decode (default 12).")
    parser.add_argument(
        "--csv",
        default="/tmp/elx808-playback.csv",
        help="CSV output path.",
    )
    args = parser.parse_args()

    fmt = args.format
    if fmt == "auto":
        fmt = _detect_format(args.log)
    if fmt == "unknown":
        print("Unable to detect log format; use --format.", file=sys.stderr)
        return 2

    if fmt == "control-stack":
        raw = _parse_control_stack_log(args.log, label=args.label)
    else:
        raw = _parse_serial_capture_log(args.log)

    if not raw:
        print("No response bytes found in log.", file=sys.stderr)
        return 2

    parsed = core.parse_response(raw)
    print(f"response: {core.format_response_summary(parsed)}")
    rows_out = stack._decode_read_plate_payload(
        parsed.data,
        wavelengths_per_interval=args.wavelengths_per_interval,
        rows=args.rows,
        cols=args.cols,
    )
    if not rows_out:
        print("No decoded rows found; check --wavelengths-per-interval/rows/cols.", file=sys.stderr)
        return 1
    stack._write_read_plate_csv(rows_out, args.csv)
    print(f"wrote csv: {args.csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
