#!/usr/bin/env python3
"""
ELx808 protocol probe (safe defaults).

Sends simple commands and logs raw responses, with basic status parsing.
Default commands are non-movement: status ('o') and basecode version ('e').
Self-test ('*') is gated behind explicit confirmation.
"""

from __future__ import annotations

import argparse
import os
import select
import sys
import time

import serial_capture as sc


def _hexdump(data: bytes) -> str:
    return " ".join(f"{b:02x}" for b in data)


def _ascii_repr(data: bytes) -> str:
    out = []
    for b in data:
        if 32 <= b < 127:
            out.append(chr(b))
        elif b == 0x0d:
            out.append("\\r")
        elif b == 0x0a:
            out.append("\\n")
        else:
            out.append(".")
    return "".join(out)


def read_response(fd: int, *, overall_timeout: float, quiet_timeout: float) -> bytes:
    start = time.monotonic()
    last_rx = None
    buf = bytearray()
    while True:
        remaining = overall_timeout - (time.monotonic() - start)
        if remaining <= 0:
            break
        timeout = min(0.25, remaining)
        r, _, _ = select.select([fd], [], [], timeout)
        if r:
            data = os.read(fd, 4096)
            if data:
                buf.extend(data)
                last_rx = time.monotonic()
                continue
        if buf and last_rx is not None and (time.monotonic() - last_rx) >= quiet_timeout:
            break
    return bytes(buf)


def _is_ascii_hex(b: int) -> bool:
    return (48 <= b <= 57) or (65 <= b <= 70)


def parse_status(candidate: bytes) -> dict | None:
    if len(candidate) != 5 or candidate[-1] != 0x03:
        return None
    if candidate[0] == 0x1E:
        code = candidate[1:4].decode("ascii", errors="replace")
        return {"mode": "312", "code": code, "raw": candidate}
    if all(_is_ascii_hex(b) for b in candidate[:4]):
        code = candidate[:4].decode("ascii", errors="replace")
        return {"mode": "ELx", "code": code, "raw": candidate}
    return None


def split_status(payload: bytes) -> tuple[bytes, bytes, dict | None]:
    etx_idx = payload.rfind(b"\x03")
    if etx_idx < 4:
        return payload, b"", None
    candidate = payload[etx_idx - 4 : etx_idx + 1]
    parsed = parse_status(candidate)
    if parsed is None:
        return payload, b"", None
    data = payload[: etx_idx - 4]
    return data, candidate, parsed


def parse_response(raw: bytes) -> dict:
    ack = raw.startswith(b"\x06")
    payload = raw[1:] if ack else raw
    data, status_raw, status_parsed = split_status(payload)
    return {
        "ack": ack,
        "data": data,
        "status": status_raw,
        "status_parsed": status_parsed,
        "raw": raw,
    }


def log_block(log, label: str, raw: bytes, parsed: dict) -> None:
    log.write(f"{label} raw_hex={_hexdump(raw)} raw_ascii={_ascii_repr(raw)}\n")
    status_tag = "none"
    if parsed["status_parsed"]:
        status_tag = f"{parsed['status_parsed']['mode']}:{parsed['status_parsed']['code']}"
    log.write(
        f"{label} ack={parsed['ack']} data_hex={_hexdump(parsed['data'])} "
        f"status_hex={_hexdump(parsed['status'])} status={status_tag}\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="ELx808 protocol probe (safe defaults).")
    parser.add_argument("--port", required=True, help="Serial device path (prefer /dev/cu.* on macOS).")
    parser.add_argument("--baud", type=int, default=9600)
    parser.add_argument("--databits", type=int, default=8, choices=[7, 8])
    parser.add_argument("--parity", default="N", choices=["N", "E", "O"])
    parser.add_argument("--stopbits", type=int, default=2, choices=[1, 2])
    parser.add_argument("--flow", default="none", choices=["none", "rtscts", "xonxoff"])
    parser.add_argument("--timeout", type=float, default=3.0, help="Overall response timeout per command.")
    parser.add_argument("--quiet", type=float, default=0.5, help="Stop after quiet period once data starts.")
    parser.add_argument("--set-dtr", type=int, choices=[0, 1], default=None)
    parser.add_argument("--set-rts", type=int, choices=[0, 1], default=None)
    parser.add_argument("--status", action="store_true", help="Send 'o' (Get Current Status).")
    parser.add_argument("--status-twice", action="store_true", help="Send 'o' twice (clears then re-reads).")
    parser.add_argument("--version", action="store_true", help="Send 'e' (Get Basecode Version).")
    parser.add_argument("--self-test", action="store_true", help="Send '*' (Self-test; movement).")
    parser.add_argument("--confirm-self-test", action="store_true", help="Acknowledge self-test movement.")
    parser.add_argument(
        "--set-status",
        choices=["elx", "312"],
        default="",
        help="Send 'n' to set status format (elx=1, 312=0) before probing.",
    )
    parser.add_argument("--log", default="", help="Write a log file (recommended).")
    args = parser.parse_args()

    if args.self_test and not args.confirm_self_test:
        print("Refusing to run self-test without --confirm-self-test (movement).", file=sys.stderr)
        return 2

    cmds: list[tuple[str, str]] = []
    if args.set_status:
        cmd = "1" if args.set_status == "elx" else "0"
        cmds.append(("n" + cmd, f"set-status-{args.set_status}"))
    if args.status or not (args.status or args.version or args.self_test):
        cmds.append(("o", "status"))
    if args.status_twice:
        cmds.append(("o", "status-2"))
    if args.version or not (args.status or args.version or args.self_test):
        cmds.append(("e", "version"))
    if args.self_test:
        cmds.append(("*", "self-test"))

    log_path = args.log
    log = open(log_path, "w", encoding="utf-8") if log_path else None

    fd = os.open(args.port, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
    try:
        sc.configure_serial(
            fd,
            baud=args.baud,
            databits=args.databits,
            parity=args.parity,
            stopbits=args.stopbits,
            flow=args.flow,
        )
        if args.set_dtr is not None:
            sc._set_modem_line(fd, "DTR", bool(args.set_dtr))
        if args.set_rts is not None:
            sc._set_modem_line(fd, "RTS", bool(args.set_rts))

        if log:
            log.write(
                f"port={args.port} baud={args.baud} databits={args.databits} "
                f"parity={args.parity} stopbits={args.stopbits} flow={args.flow}\n"
            )
            log.write(f"start={time.strftime('%Y-%m-%dT%H:%M:%S%z')}\n")
            log.flush()

        for cmd, label in cmds:
            os.write(fd, cmd.encode("ascii"))
            raw = read_response(fd, overall_timeout=args.timeout, quiet_timeout=args.quiet)
            parsed = parse_response(raw)
            status_tag = "none"
            if parsed["status_parsed"]:
                status_tag = f"{parsed['status_parsed']['mode']}:{parsed['status_parsed']['code']}"
            print(
                f"{label}: ack={parsed['ack']} data_hex={_hexdump(parsed['data'])} "
                f"status_hex={_hexdump(parsed['status'])} status={status_tag}"
            )
            if log:
                log_block(log, label, raw, parsed)
                log.flush()
            time.sleep(0.2)
    finally:
        if log:
            log.close()
        os.close(fd)

    if log_path:
        print(f"Wrote log: {log_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
