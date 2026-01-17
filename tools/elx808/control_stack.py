#!/usr/bin/env python3
"""
Minimal ELx808 control stack (transport + protocol wrapper).

Safe-by-default: read-only commands require no extra flags; state-changing
commands require explicit confirmation.
"""

from __future__ import annotations

import argparse
import os
import sys
import time

import elx808_core as core
import serial_capture as sc


def _parse_send_arg(value: str) -> bytes:
    if value == "CR":
        return b"\r"
    if value == "LF":
        return b"\n"
    if value == "CRLF":
        return b"\r\n"
    if value.startswith("HEX:"):
        hex_bytes = value[4:].strip()
        parts = [p for p in hex_bytes.replace(",", " ").split(" ") if p]
        return bytes(int(p, 16) for p in parts)
    return value.encode("ascii", errors="replace")


def _parse_well(value: str) -> tuple[int, int]:
    text = value.strip().upper()
    if not text:
        raise ValueError("Well cannot be empty.")
    if text[0].isalpha():
        row_char = text[0]
        if row_char < "A" or row_char > "P":
            raise ValueError(f"Well row out of range (A-P): {value}")
        row = ord(row_char) - ord("A") + 1
        col_text = text[1:]
        if not col_text:
            raise ValueError(f"Well column missing: {value}")
        col = int(col_text, 10)
    else:
        if "," in text:
            parts = text.split(",", 1)
        elif ":" in text:
            parts = text.split(":", 1)
        else:
            raise ValueError(f"Well must be like A1 or 01,01: {value}")
        row = int(parts[0], 10)
        col = int(parts[1], 10)
    if not (1 <= row <= 16):
        raise ValueError(f"Well row out of range (1-16): {value}")
    if not (1 <= col <= 24):
        raise ValueError(f"Well column out of range (1-24): {value}")
    return row, col


def _encode_well(row: int, col: int) -> bytes:
    return f"{row:02d}{col:02d}".encode("ascii")


def _build_well_payload(wells: list[str], position: int) -> bytes:
    if not wells:
        raise ValueError("Provide at least one --well (A1, B3, 01,01).")
    if len(wells) > 8:
        raise ValueError("Up to 8 wells are supported per read-wells request.")
    payload = bytearray()
    for item in wells:
        row, col = _parse_well(item)
        payload.extend(_encode_well(row, col))
    for _ in range(8 - len(wells)):
        payload.extend(b"0000")
    payload.extend(str(position).encode("ascii"))
    if len(payload) != 33:
        raise ValueError(f"Unexpected read-wells payload length: {len(payload)}")
    return bytes(payload)


def _parse_hex_string(value: str) -> bytes:
    parts = [p for p in value.replace(",", " ").split(" ") if p]
    return bytes(int(part, 16) for part in parts)


def _load_payload(payload_hex: str | None, payload_file: str | None) -> bytes:
    if payload_file:
        with open(payload_file, "rb") as handle:
            return handle.read()
    if payload_hex:
        return _parse_hex_string(payload_hex)
    raise ValueError("Provide --payload-hex or --payload-file for read commands.")


def _build_command(args: argparse.Namespace) -> tuple[str, bytes, bool, bool, bool]:
    if args.command == "status":
        return "status", b"o", False, False, False
    if args.command == "version":
        return "version", b"e", False, False, False
    if args.command == "set-status":
        cmd = b"n1" if args.mode == "elx" else b"n0"
        return f"set-status-{args.mode}", cmd, True, False, False
    if args.command == "quiet":
        cmd = b"q1" if args.mode == "on" else b"q0"
        return f"quiet-{args.mode}", cmd, True, False, False
    if args.command == "self-test":
        return "self-test", b"*", False, True, False
    if args.command == "raw":
        payload = _parse_send_arg(args.payload)
        return "raw", payload, True, False, False
    if args.command == "read-plate":
        return "read-plate", b"S", True, True, True
    if args.command == "read-wells":
        if args.payload_hex or args.payload_file:
            if args.well:
                raise ValueError("Use --payload-* or --well, not both.")
            payload = _load_payload(args.payload_hex, args.payload_file)
        else:
            payload = _build_well_payload(args.well, args.position)
        if len(payload) != 33:
            raise ValueError(f"read-wells payload must be 33 bytes, got {len(payload)}.")
        return "read-wells", payload, True, True, True
    raise ValueError(f"Unsupported command: {args.command}")


def _require_confirmation(
    args: argparse.Namespace, needs_write: bool, needs_movement: bool, needs_read: bool
) -> int:
    if needs_movement and not args.confirm_movement:
        print("Refusing to run movement command without --confirm-movement.", file=sys.stderr)
        return 2
    if needs_write and not args.confirm_write:
        print("Refusing to run state-changing command without --confirm-write.", file=sys.stderr)
        return 2
    if needs_read and not args.confirm_read:
        print("Refusing to run read command without --confirm-read.", file=sys.stderr)
        return 2
    return 0


def _log_tx(log, label: str, payload: bytes) -> None:
    if not log:
        return
    log.write(
        f"cmd={label} tx_hex={core.hexdump(payload)} "
        f"tx_ascii={core.ascii_repr(payload)}\n"
    )
    log.flush()


def _describe_read_payload(label: str, parsed: core.Response, log) -> None:
    if not parsed.data:
        return
    if parsed.data == bytes([core.DLE]):
        print(f"{label}-data: DLE (read aborted)")
        if log:
            log.write(f"{label}-data DLE\n")
        return
    initial_status, remainder = core.split_leading_status(parsed.data)
    if initial_status:
        print(
            f"{label}-initial-status: {initial_status.mode}:{initial_status.code}"
        )
        if log:
            log.write(
                f"{label}-initial-status {initial_status.mode}:{initial_status.code}\n"
            )
    blocks, complete, trailing = core.parse_elx_wavelength_blocks(remainder)
    if blocks:
        summary = f"blocks={len(blocks)} complete={complete} trailing_hex={core.hexdump(trailing)}"
        print(f"{label}-blocks: {summary}")
        if log:
            log.write(f"{label}-blocks {summary}\n")
        return
    if remainder:
        summary = f"data_len={len(remainder)} data_hex={core.hexdump(remainder)}"
        print(f"{label}-data: {summary}")
        if log:
            log.write(f"{label}-data {summary}\n")


def _handle_response(label: str, raw: bytes, *, log, parse_read: bool) -> core.Response:
    parsed = core.parse_response(raw)
    print(f"{label}: {core.format_response_summary(parsed)}")
    if log:
        core.log_block(log, label, raw, parsed)
        log.flush()
    if parse_read:
        _describe_read_payload(label, parsed, log)
    return parsed


def _read_response_with_continuation(
    fd: int, *, overall_timeout: float, quiet_timeout: float
) -> bytes:
    raw = core.read_response(fd, overall_timeout=overall_timeout, quiet_timeout=quiet_timeout)
    if raw == bytes([core.ACK]):
        more = core.read_response(fd, overall_timeout=overall_timeout, quiet_timeout=quiet_timeout)
        raw = raw + more
    return raw


def _run_simple_command(
    fd: int,
    label: str,
    payload: bytes,
    timeout: float,
    quiet: float,
    log,
) -> None:
    _log_tx(log, label, payload)
    os.write(fd, payload)
    raw = core.read_response(fd, overall_timeout=timeout, quiet_timeout=quiet)
    _handle_response(label, raw, log=log, parse_read=False)
    time.sleep(0.2)


def _run_read_plate(
    fd: int,
    label: str,
    payload: bytes,
    timeout: float,
    quiet: float,
    log,
) -> None:
    _log_tx(log, label, payload)
    os.write(fd, payload)
    raw = _read_response_with_continuation(
        fd, overall_timeout=timeout, quiet_timeout=quiet
    )
    _handle_response(label, raw, log=log, parse_read=True)
    time.sleep(0.2)


def _run_read_wells(
    fd: int,
    label: str,
    payload: bytes,
    timeout: float,
    quiet: float,
    log,
) -> None:
    _log_tx(log, f"{label}-cmd", b"d")
    os.write(fd, b"d")
    raw = core.read_response(fd, overall_timeout=min(1.0, timeout), quiet_timeout=0.2)
    ack = _handle_response(f"{label}-cmd", raw, log=log, parse_read=False)
    if not ack.ack:
        print(f"{label}: no ACK for command, aborting.")
        return
    packet = payload + bytes([core.ETX])
    _log_tx(log, f"{label}-payload", packet)
    os.write(fd, packet)
    raw = _read_response_with_continuation(
        fd, overall_timeout=timeout, quiet_timeout=quiet
    )
    _handle_response(label, raw, log=log, parse_read=True)
    time.sleep(0.2)


def _run_commands(
    fd: int,
    commands: list[tuple[str, bytes]],
    *,
    timeout: float,
    quiet: float,
    log,
) -> None:
    for label, payload in commands:
        if label == "read-plate":
            _run_read_plate(fd, label, payload, timeout, quiet, log)
            continue
        if label == "read-wells":
            _run_read_wells(fd, label, payload, timeout, quiet, log)
            continue
        _run_simple_command(fd, label, payload, timeout, quiet, log)


def main() -> int:
    parser = argparse.ArgumentParser(description="ELx808 control stack (minimal, safe-by-default).")
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
    parser.add_argument("--log", default="", help="Write a log file.")
    parser.add_argument(
        "--confirm-write",
        action="store_true",
        help="Required for state-changing commands (quiet/status format/raw).",
    )
    parser.add_argument(
        "--confirm-movement",
        action="store_true",
        help="Required for movement commands (self-test, carrier moves).",
    )
    parser.add_argument(
        "--confirm-read",
        action="store_true",
        help="Required for read commands (read-plate/read-wells).",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("status", help="Get current status ('o').")
    sub.add_parser("version", help="Get basecode version ('e').")
    status = sub.add_parser("set-status", help="Set status format ('n').")
    status.add_argument("mode", choices=["elx", "312"])
    quiet = sub.add_parser("quiet", help="Set quiet mode ('q').")
    quiet.add_argument("mode", choices=["on", "off"])
    sub.add_parser("self-test", help="Run self-test ('*') (movement).")
    raw = sub.add_parser("raw", help="Send raw payload (ASCII or HEX:..).")
    raw.add_argument("payload", help="Text, CR/LF/CRLF, or HEX:01 02 ...")
    sub.add_parser("read-plate", help="Read plate ('S') with current assay definition.")
    read_wells = sub.add_parser("read-wells", help="Read well set ('d') for up to 8 wells.")
    read_wells.add_argument(
        "--well",
        action="append",
        default=[],
        help="Well identifier like A1 or 01,01 (repeat up to 8).",
    )
    read_wells.add_argument(
        "--position",
        type=int,
        default=0,
        choices=[0, 1, 2, 3],
        help="Read series position: 0 single, 1 first, 2 next, 3 final.",
    )
    read_wells.add_argument(
        "--payload-hex",
        default="",
        help="Override with hex bytes for the well-set request (33 bytes).",
    )
    read_wells.add_argument(
        "--payload-file",
        default="",
        help="Override with binary payload file for the well-set request (33 bytes).",
    )
    sequence = sub.add_parser(
        "sequence",
        help="Run set-status -> status -> version in one session.",
    )
    sequence.add_argument("--mode", choices=["elx", "312"], default="elx")
    sequence.add_argument(
        "--skip-set-status",
        action="store_true",
        help="Skip status format change; only run status and version.",
    )

    args, unknown = parser.parse_known_args()
    if "--confirm-write" in unknown:
        args.confirm_write = True
    if "--confirm-movement" in unknown:
        args.confirm_movement = True
    if "--confirm-read" in unknown:
        args.confirm_read = True
    unknown = [
        item
        for item in unknown
        if item not in ("--confirm-write", "--confirm-movement", "--confirm-read")
    ]
    if unknown:
        parser.error(f"unrecognized arguments: {' '.join(unknown)}")
    commands: list[tuple[str, bytes]] = []
    needs_write = False
    needs_movement = False
    needs_read = False
    try:
        if args.command == "sequence":
            if not args.skip_set_status:
                label = f"set-status-{args.mode}"
                payload = b"n1" if args.mode == "elx" else b"n0"
                commands.append((label, payload))
                needs_write = True
            for cmd_label in ("status", "version"):
                label, payload, write, movement, read = _build_command(
                    argparse.Namespace(command=cmd_label)
                )
                commands.append((label, payload))
                needs_write = needs_write or write
                needs_movement = needs_movement or movement
                needs_read = needs_read or read
        else:
            label, payload, needs_write, needs_movement, needs_read = _build_command(args)
            commands = [(label, payload)]
    except ValueError as exc:
        parser.error(str(exc))

    confirmation = _require_confirmation(args, needs_write, needs_movement, needs_read)
    if confirmation:
        return confirmation

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

        _run_commands(fd, commands, timeout=args.timeout, quiet=args.quiet, log=log)
    finally:
        if log:
            log.close()
        os.close(fd)

    if log_path:
        print(f"Wrote log: {log_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
