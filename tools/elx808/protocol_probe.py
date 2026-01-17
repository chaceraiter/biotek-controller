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
import sys
import time

import elx808_core as core
import serial_capture as sc


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
            raw = core.read_response(fd, overall_timeout=args.timeout, quiet_timeout=args.quiet)
            parsed = core.parse_response(raw)
            print(f"{label}: {core.format_response_summary(parsed)}")
            if log:
                core.log_block(log, label, raw, parsed)
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
