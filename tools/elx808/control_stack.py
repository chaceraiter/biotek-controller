#!/usr/bin/env python3
"""
Minimal ELx808 control stack (transport + protocol wrapper).

Safe-by-default: read-only commands require no extra flags; state-changing
commands require explicit confirmation.
"""

from __future__ import annotations

import argparse
import os
import select
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


def _write_bytes(buf: bytearray, pos: int, data: bytes) -> None:
    start = pos - 1
    buf[start : start + len(data)] = data


def _encode_ascii(value: str, length: int) -> bytes:
    encoded = value.encode("ascii", errors="replace")
    if len(encoded) > length:
        raise ValueError(f"Value too long (max {length} bytes): {value}")
    return encoded.ljust(length, b" ")


def _encode_wavelength(value: int) -> bytes:
    if value == 0:
        return b"000"
    if value < 340 or value > 900:
        raise ValueError(f"Wavelength out of range (340-900 or 0): {value}")
    return f"{value:03d}".encode("ascii")


def _encode_u16(
    value: int, *, field: str, min_value: int, max_value: int, allow_zero: bool
) -> bytes:
    if value == 0 and allow_zero:
        return b"\x00\x00"
    if value < min_value or value > max_value:
        raise ValueError(f"{field} out of range ({min_value}-{max_value}): {value}")
    return value.to_bytes(2, "little")


def _load_assay_profiles(path: str) -> dict:
    import json

    try:
        with open(path, "r", encoding="utf-8") as handle:
            data = json.load(handle)
    except FileNotFoundError as exc:
        raise ValueError(f"Profile file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Profile file is not valid JSON: {path}") from exc
    if not isinstance(data, dict):
        raise ValueError("Profile file must contain a JSON object.")
    return data


def _apply_assay_profile(
    args: argparse.Namespace, *, profile_name: str, profile_file: str, provided_flags: set[str]
) -> None:
    profiles = _load_assay_profiles(profile_file)
    if profile_name not in profiles:
        raise ValueError(f"Profile not found: {profile_name}")
    profile = profiles[profile_name]
    if not isinstance(profile, dict):
        raise ValueError(f"Profile must be an object: {profile_name}")

    allowed_keys = {
        "assay_name",
        "measurement_wavelength",
        "reference_wavelength",
        "wavelength",
        "read_type",
        "subtraction",
        "scan_points",
        "kinetic_interval",
        "kinetic_read_count",
        "use_total_kinetic_time",
        "total_kinetic_read_time",
        "shake",
        "shake_every_read",
        "shake_continuous",
        "shake_time",
        "shake_speed",
        "delay_seconds",
        "delay_enabled",
    }
    unknown = sorted(key for key in profile.keys() if key not in allowed_keys)
    if unknown:
        raise ValueError(f"Unknown profile keys: {', '.join(unknown)}")

    flag_map = {
        "assay_name": "--assay-name",
        "measurement_wavelength": "--measurement-wavelength",
        "reference_wavelength": "--reference-wavelength",
        "wavelength": "--wavelength",
        "read_type": "--read-type",
        "subtraction": "--subtraction",
        "scan_points": "--scan-points",
        "kinetic_interval": "--kinetic-interval",
        "kinetic_read_count": "--kinetic-read-count",
        "use_total_kinetic_time": "--use-total-kinetic-time",
        "total_kinetic_read_time": "--total-kinetic-read-time",
        "shake": "--shake",
        "shake_every_read": "--shake-every-read",
        "shake_continuous": "--shake-continuous",
        "shake_time": "--shake-time",
        "shake_speed": "--shake-speed",
        "delay_seconds": "--delay-seconds",
        "delay_enabled": "--delay-enabled",
    }

    def should_override(key: str) -> bool:
        flag = flag_map.get(key)
        return flag is None or flag not in provided_flags

    if should_override("assay_name"):
        args.assay_name = profile.get("assay_name") or profile_name
    if should_override("measurement_wavelength") and "measurement_wavelength" in profile:
        args.measurement_wavelength = int(profile["measurement_wavelength"])
    if should_override("reference_wavelength") and "reference_wavelength" in profile:
        args.reference_wavelength = int(profile["reference_wavelength"])
    if should_override("wavelength") and "wavelength" in profile:
        wavelengths = profile["wavelength"]
        if isinstance(wavelengths, list):
            args.wavelength = [int(value) for value in wavelengths]
        elif wavelengths is None:
            args.wavelength = []
        else:
            args.wavelength = [int(wavelengths)]
    if should_override("read_type") and "read_type" in profile:
        args.read_type = str(profile["read_type"])
    if should_override("subtraction") and "subtraction" in profile:
        args.subtraction = str(profile["subtraction"])
    if should_override("scan_points") and "scan_points" in profile:
        args.scan_points = int(profile["scan_points"])
    if should_override("kinetic_interval") and "kinetic_interval" in profile:
        args.kinetic_interval = int(profile["kinetic_interval"])
    if should_override("kinetic_read_count") and "kinetic_read_count" in profile:
        args.kinetic_read_count = int(profile["kinetic_read_count"])
    if should_override("use_total_kinetic_time") and "use_total_kinetic_time" in profile:
        args.use_total_kinetic_time = bool(profile["use_total_kinetic_time"])
    if should_override("total_kinetic_read_time") and "total_kinetic_read_time" in profile:
        args.total_kinetic_read_time = int(profile["total_kinetic_read_time"])
    if should_override("shake") and "shake" in profile:
        args.shake = bool(profile["shake"])
    if should_override("shake_every_read") and "shake_every_read" in profile:
        args.shake_every_read = bool(profile["shake_every_read"])
    if should_override("shake_continuous") and "shake_continuous" in profile:
        args.shake_continuous = bool(profile["shake_continuous"])
    if should_override("shake_time") and "shake_time" in profile:
        args.shake_time = int(profile["shake_time"])
    if should_override("shake_speed") and "shake_speed" in profile:
        args.shake_speed = int(profile["shake_speed"])
    if should_override("delay_seconds") and "delay_seconds" in profile:
        args.delay_seconds = int(profile["delay_seconds"])
    if should_override("delay_enabled") and "delay_enabled" in profile:
        value = profile["delay_enabled"]
        args.delay_enabled = None if value is None else int(value)


def _default_assay_args() -> argparse.Namespace:
    return argparse.Namespace(
        assay_name="",
        measurement_wavelength=None,
        reference_wavelength=0,
        wavelength=[],
        read_type="endpoint",
        subtraction="none",
        scan_points=1,
        kinetic_interval=None,
        kinetic_read_count=None,
        use_total_kinetic_time=False,
        total_kinetic_read_time=None,
        shake=False,
        shake_every_read=False,
        shake_continuous=False,
        shake_time=0,
        shake_speed=0,
        delay_seconds=0,
        delay_enabled=None,
    )


def _load_assay_from_profile(profile_name: str, profile_file: str) -> argparse.Namespace:
    args = _default_assay_args()
    _apply_assay_profile(
        args,
        profile_name=profile_name,
        profile_file=profile_file,
        provided_flags=set(),
    )
    if not args.assay_name:
        raise ValueError("--assay-name is required unless --profile provides one.")
    return args


def _estimate_kinetic_duration_seconds(args: argparse.Namespace) -> float | None:
    if args.read_type != "kinetic":
        return None
    if args.use_total_kinetic_time and args.total_kinetic_read_time:
        return float(args.total_kinetic_read_time) * 60.0
    if args.kinetic_interval and args.kinetic_read_count:
        return float(args.kinetic_interval) * float(args.kinetic_read_count)
    return None


def _flag_present(flags: set[str], name: str) -> bool:
    if name in flags:
        return True
    return any(flag.startswith(f"{name}=") for flag in flags)


def _expected_intervals(args: argparse.Namespace) -> int | None:
    if args.read_type != "kinetic":
        return None
    if args.kinetic_read_count:
        return int(args.kinetic_read_count)
    if (
        args.use_total_kinetic_time
        and args.total_kinetic_read_time
        and args.kinetic_interval
    ):
        total_seconds = float(args.total_kinetic_read_time) * 60.0
        return int((total_seconds + args.kinetic_interval - 1) // args.kinetic_interval)
    return None


def _build_assay_definition(args: argparse.Namespace) -> bytes:
    buf = bytearray(170)
    _write_bytes(buf, 1, b"\x00")
    _write_bytes(buf, 2, _encode_ascii(args.assay_name, 6))

    subtraction = 0x40 if args.subtraction == "dual" else 0x00
    _write_bytes(buf, 30, bytes([subtraction]))

    flags = 0x00
    if args.shake:
        flags |= 0x10
    if args.shake_every_read:
        flags |= 0x20
    if args.shake_continuous:
        flags |= 0x40
    if args.use_total_kinetic_time:
        flags |= 0x80
    _write_bytes(buf, 31, bytes([flags]))

    scan_points = args.scan_points
    if scan_points < 1 or scan_points > 31 or scan_points % 2 == 0:
        raise ValueError("scan-points must be odd, between 1 and 31.")
    _write_bytes(buf, 32, bytes([scan_points]))

    read_type_map = {"endpoint": 0, "kinetic": 2, "scan1d": 3}
    read_type = read_type_map[args.read_type]
    _write_bytes(buf, 56, bytes([read_type]))

    measurement = args.measurement_wavelength
    if args.wavelength:
        if measurement not in (None, 0):
            raise ValueError("measurement-wavelength must be 0 when using --wavelength.")
        measurement = 0
    if measurement is None:
        raise ValueError("measurement-wavelength is required when not using --wavelength.")
    if not args.wavelength and measurement == 0:
        raise ValueError("measurement-wavelength cannot be 0 unless --wavelength is used.")
    _write_bytes(buf, 50, _encode_wavelength(measurement))

    reference = args.reference_wavelength or 0
    if args.subtraction == "dual" and reference == 0:
        raise ValueError("reference-wavelength is required for dual subtraction.")
    _write_bytes(buf, 53, _encode_wavelength(reference))

    if args.read_type == "kinetic":
        if args.kinetic_interval is None:
            raise ValueError("kinetic-interval is required for kinetic reads.")
        if args.use_total_kinetic_time and args.total_kinetic_read_time is None:
            raise ValueError("total-kinetic-read-time is required when using total kinetic time.")
        if not args.use_total_kinetic_time and args.kinetic_read_count is None:
            raise ValueError("kinetic-read-count is required for kinetic reads.")

    kinetic_interval = args.kinetic_interval or 0
    _write_bytes(
        buf,
        60,
        _encode_u16(
            kinetic_interval,
            field="kinetic-interval",
            min_value=0,
            max_value=9999,
            allow_zero=True,
        ),
    )

    kinetic_read_count = args.kinetic_read_count or 0
    _write_bytes(
        buf,
        62,
        _encode_u16(
            kinetic_read_count,
            field="kinetic-read-count",
            min_value=2,
            max_value=9999,
            allow_zero=True,
        ),
    )

    wavelengths = args.wavelength or []
    if len(wavelengths) > 6:
        raise ValueError("At most 6 wavelengths are supported for --wavelength.")
    padded = wavelengths + [0] * (6 - len(wavelengths))
    _write_bytes(buf, 67, _encode_wavelength(padded[0]))
    remaining = b"".join(_encode_wavelength(val) for val in padded[1:])
    _write_bytes(buf, 70, remaining)

    shake_time = args.shake_time or 0
    _write_bytes(
        buf,
        163,
        _encode_u16(
            shake_time,
            field="shake-time",
            min_value=0,
            max_value=999,
            allow_zero=True,
        ),
    )
    _write_bytes(buf, 165, bytes([args.shake_speed]))

    total_kinetic_time = args.total_kinetic_read_time or 0
    _write_bytes(
        buf,
        166,
        _encode_u16(
            total_kinetic_time,
            field="total-kinetic-read-time",
            min_value=1,
            max_value=9999,
            allow_zero=True,
        ),
    )

    delay_seconds = args.delay_seconds or 0
    delay_enabled = args.delay_enabled
    if delay_enabled is None:
        delay_enabled = 1 if delay_seconds > 0 else 0
    _write_bytes(buf, 168, bytes([1 if delay_enabled else 0]))
    _write_bytes(
        buf,
        169,
        _encode_u16(
            delay_seconds,
            field="delay-seconds",
            min_value=0,
            max_value=999,
            allow_zero=True,
        ),
    )
    return bytes(buf)

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


def _build_command(args: argparse.Namespace) -> tuple[str, bytes, bool, bool, bool, bool]:
    if args.command == "status":
        return "status", b"o", False, False, False, False
    if args.command == "version":
        return "version", b"e", False, False, False, False
    if args.command == "set-status":
        cmd = b"n1" if args.mode == "elx" else b"n0"
        return f"set-status-{args.mode}", cmd, True, False, False, False
    if args.command == "quiet":
        cmd = b"q1" if args.mode == "on" else b"q0"
        return f"quiet-{args.mode}", cmd, True, False, False, False
    if args.command == "self-test":
        return "self-test", b"*", False, True, False, False
    if args.command == "raw":
        payload = _parse_send_arg(args.payload)
        return "raw", payload, True, False, False, False
    if args.command == "read-plate":
        return "read-plate", b"S", True, True, True, False
    if args.command == "read-wells":
        if args.payload_hex or args.payload_file:
            if args.well:
                raise ValueError("Use --payload-* or --well, not both.")
            payload = _load_payload(args.payload_hex, args.payload_file)
        else:
            payload = _build_well_payload(args.well, args.position)
        if len(payload) != 33:
            raise ValueError(f"read-wells payload must be 33 bytes, got {len(payload)}.")
        return "read-wells", payload, True, True, True, False
    if args.command == "get-wavelengths":
        return "get-wavelengths", b"W", False, False, False, False
    if args.command == "set-assay":
        payload = _build_assay_definition(args)
        return "set-assay", payload, True, False, False, True
    raise ValueError(f"Unsupported command: {args.command}")


def _require_confirmation(
    args: argparse.Namespace,
    needs_write: bool,
    needs_movement: bool,
    needs_read: bool,
    needs_assay: bool,
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
    if needs_assay and not args.confirm_assay:
        print("Refusing to run assay definition without --confirm-assay.", file=sys.stderr)
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


def _parse_well_value(token: bytes) -> tuple[float | None, str]:
    if token == b"*****":
        return None, "overrange"
    if len(token) != 5:
        return None, "invalid"
    sign = token[:1]
    digits = token[1:]
    if sign not in (b"+", b"-") or not digits.isdigit():
        return None, "invalid"
    value = int(digits) / 1000.0
    if sign == b"-":
        value = -value
    return value, "ok"


def _parse_plate_row(line: bytes, cols: int) -> tuple[list[float | None], list[str]]:
    parts = line.split(b",")
    if parts and parts[0] == b"":
        parts = parts[1:]
    values: list[float | None] = []
    statuses: list[str] = []
    for part in parts[:cols]:
        value, status = _parse_well_value(part)
        values.append(value)
        statuses.append(status)
    while len(values) < cols:
        values.append(None)
        statuses.append("missing")
    return values, statuses


def _parse_plate_block(
    payload: bytes, *, rows: int, cols: int
) -> tuple[list[list[float | None]], list[list[str]], float | None]:
    if payload.startswith(b"\r"):
        payload = payload[1:]
    lines = payload.split(b"\r\n")
    temp = None
    if lines and len(lines[-1]) == 3 and lines[-1].isdigit():
        temp = int(lines[-1]) / 10.0
        lines = lines[:-1]
    values_rows: list[list[float | None]] = []
    status_rows: list[list[str]] = []
    for line in lines:
        if not line:
            continue
        values, statuses = _parse_plate_row(line, cols)
        values_rows.append(values)
        status_rows.append(statuses)
        if len(values_rows) >= rows:
            break
    while len(values_rows) < rows:
        values_rows.append([None] * cols)
        status_rows.append(["missing"] * cols)
    return values_rows, status_rows, temp


def _decode_read_plate_payload(
    data: bytes, *, wavelengths_per_interval: int, rows: int, cols: int
) -> list[dict]:
    initial_status, remainder = core.split_leading_status(data)
    _ = initial_status
    blocks, _, _ = core.parse_elx_wavelength_blocks(remainder)
    if wavelengths_per_interval < 1:
        wavelengths_per_interval = 1
    rows_out: list[dict] = []
    for block_index, block in enumerate(blocks):
        values_rows, status_rows, temp = _parse_plate_block(
            block.payload, rows=rows, cols=cols
        )
        interval_index = block_index // wavelengths_per_interval + 1
        wavelength_index = block_index % wavelengths_per_interval + 1
        for r in range(rows):
            row_letter = chr(ord("A") + r)
            for c in range(cols):
                rows_out.append(
                    {
                        "interval": interval_index,
                        "wavelength_index": wavelength_index,
                        "row": r + 1,
                        "col": c + 1,
                        "well": f"{row_letter}{c + 1}",
                        "value": values_rows[r][c],
                        "status": status_rows[r][c],
                        "temperature": temp,
                    }
                )
    return rows_out


def _summarize_read_plate(
    data: bytes, *, wavelengths_per_interval: int
) -> tuple[int, int, bool]:
    _, remainder = core.split_leading_status(data)
    blocks, complete, _ = core.parse_elx_wavelength_blocks(remainder)
    if wavelengths_per_interval < 1:
        wavelengths_per_interval = 1
    interval_count = 0
    if blocks:
        interval_count = (len(blocks) + wavelengths_per_interval - 1) // wavelengths_per_interval
    return interval_count, len(blocks), complete


def _write_read_plate_csv(rows: list[dict], path: str) -> None:
    import csv

    with open(path, "w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "interval",
                "wavelength_index",
                "row",
                "col",
                "well",
                "value",
                "status",
                "temperature_c",
            ]
        )
        for row in rows:
            value = "" if row["value"] is None else f"{row['value']:.3f}"
            temp = "" if row["temperature"] is None else f"{row['temperature']:.1f}"
            writer.writerow(
                [
                    row["interval"],
                    row["wavelength_index"],
                    row["row"],
                    row["col"],
                    row["well"],
                    value,
                    row["status"],
                    temp,
                ]
            )


class _IncrementalPlateCsvWriter:
    def __init__(self, path: str, *, rows: int, cols: int) -> None:
        import csv

        self._rows = rows
        self._cols = cols
        self._handle = open(path, "w", encoding="utf-8", newline="")
        self._writer = csv.writer(self._handle)
        self._writer.writerow(
            [
                "interval",
                "wavelength_index",
                "row",
                "col",
                "well",
                "value",
                "status",
                "temperature_c",
            ]
        )

    def write_block(
        self, payload: bytes, *, interval_index: int, wavelength_index: int
    ) -> int:
        values_rows, status_rows, temp = _parse_plate_block(
            payload, rows=self._rows, cols=self._cols
        )
        for r in range(self._rows):
            row_letter = chr(ord("A") + r)
            for c in range(self._cols):
                value = values_rows[r][c]
                temp_value = "" if temp is None else f"{temp:.1f}"
                value_str = "" if value is None else f"{value:.3f}"
                self._writer.writerow(
                    [
                        interval_index,
                        wavelength_index,
                        r + 1,
                        c + 1,
                        f"{row_letter}{c + 1}",
                        value_str,
                        status_rows[r][c],
                        temp_value,
                    ]
                )
        self._handle.flush()
        return self._rows * self._cols

    def close(self) -> None:
        self._handle.close()


def _parse_well_block(payload: bytes) -> tuple[list[float | None], list[str], float | None]:
    idx = payload.find(b"\r")
    if idx == -1:
        idx = 0
    else:
        idx += 1
    values: list[float | None] = []
    statuses: list[str] = []
    for _ in range(8):
        if idx >= len(payload):
            break
        if payload[idx : idx + 1] != b",":
            next_comma = payload.find(b",", idx)
            if next_comma == -1:
                break
            idx = next_comma
        idx += 1
        token = payload[idx : idx + 5]
        if len(token) < 5:
            break
        value, status = _parse_well_value(token)
        values.append(value)
        statuses.append(status)
        idx += 5
    while len(values) < 8:
        values.append(None)
        statuses.append("missing")
    temp = None
    if idx + 2 <= len(payload) and payload[idx : idx + 2] == b"\r\n":
        idx += 2
        if idx + 3 <= len(payload):
            temp_bytes = payload[idx : idx + 3]
            if temp_bytes.isdigit():
                temp = int(temp_bytes) / 10.0
    return values, statuses, temp


def _decode_read_wells_payload(
    data: bytes, *, wavelengths_per_interval: int, well_labels: list[str]
) -> list[dict]:
    initial_status, remainder = core.split_leading_status(data)
    _ = initial_status
    blocks, _, _ = core.parse_elx_wavelength_blocks(remainder)
    rows: list[dict] = []
    if wavelengths_per_interval < 1:
        wavelengths_per_interval = 1
    for block_index, block in enumerate(blocks):
        values, statuses, temp = _parse_well_block(block.payload)
        interval_index = block_index // wavelengths_per_interval + 1
        wavelength_index = block_index % wavelengths_per_interval + 1
        for i in range(8):
            label = well_labels[i] if i < len(well_labels) else f"W{i + 1}"
            rows.append(
                {
                    "interval": interval_index,
                    "wavelength_index": wavelength_index,
                    "well_index": i + 1,
                    "well_label": label,
                    "value": values[i],
                    "status": statuses[i],
                    "temperature": temp,
                }
            )
    return rows


def _write_read_wells_csv(rows: list[dict], path: str) -> None:
    import csv

    with open(path, "w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "interval",
                "wavelength_index",
                "well_index",
                "well_label",
                "value",
                "status",
                "temperature_c",
            ]
        )
        for row in rows:
            value = "" if row["value"] is None else f"{row['value']:.3f}"
            temp = "" if row["temperature"] is None else f"{row['temperature']:.1f}"
            writer.writerow(
                [
                    row["interval"],
                    row["wavelength_index"],
                    row["well_index"],
                    row["well_label"],
                    value,
                    row["status"],
                    temp,
                ]
            )


def _parse_wavelength_table(data: bytes) -> list[int]:
    text = data.decode("ascii", errors="replace").strip()
    if not text:
        return []
    parts = [p for p in text.split(",") if p]
    values: list[int] = []
    for part in parts:
        part = part.strip()
        if not part:
            continue
        try:
            values.append(int(part))
        except ValueError:
            continue
    return values


def _read_response_with_continuation(
    fd: int, *, overall_timeout: float, quiet_timeout: float
) -> bytes:
    raw = core.read_response(fd, overall_timeout=overall_timeout, quiet_timeout=quiet_timeout)
    if raw == bytes([core.ACK]):
        more = core.read_response(fd, overall_timeout=overall_timeout, quiet_timeout=quiet_timeout)
        raw = raw + more
    return raw


def _read_plate_streaming(
    fd: int,
    *,
    overall_timeout: float,
    quiet_timeout: float,
    wavelengths_per_interval: int,
    rows: int,
    cols: int,
    csv_path: str,
    label: str,
) -> tuple[bytes, int, bool]:
    raw = bytearray()
    buf = bytearray()
    ack_seen = False
    leading_status_stripped = False
    block_index = 0
    done_marker = False
    complete_seen = False
    effective_quiet = quiet_timeout
    writer = _IncrementalPlateCsvWriter(csv_path, rows=rows, cols=cols)
    if wavelengths_per_interval < 1:
        wavelengths_per_interval = 1
    start = time.monotonic()
    last_rx = None
    try:
        while True:
            remaining = overall_timeout - (time.monotonic() - start)
            if remaining <= 0:
                break
            timeout = min(0.25, remaining)
            readable, _, _ = select.select([fd], [], [], timeout)
            if readable:
                data = os.read(fd, 4096)
                if not data:
                    continue
                raw.extend(data)
                buf.extend(data)
                last_rx = time.monotonic()
                if not ack_seen and buf:
                    if buf[0] in (core.ACK, core.NAK):
                        ack_seen = True
                        if buf[0] == core.NAK:
                            buf = buf[1:]
                            return bytes(raw), block_index
                        buf = buf[1:]
                if not leading_status_stripped and len(buf) >= 5:
                    status = core.parse_status(buf[:5])
                    if status:
                        leading_status_stripped = True
                        buf = buf[5:]
                while True:
                    blocks, complete, trailing = core.parse_elx_wavelength_blocks(buf)
                    if not blocks:
                        buf = trailing
                        break
                    for block in blocks:
                        interval_index = block_index // wavelengths_per_interval + 1
                        wavelength_index = block_index % wavelengths_per_interval + 1
                        rows_written = writer.write_block(
                            block.payload,
                            interval_index=interval_index,
                            wavelength_index=wavelength_index,
                        )
                        print(
                            f"{label}-interval {interval_index} "
                            f"wavelength {wavelength_index}/{wavelengths_per_interval}: "
                            f"wrote {rows_written} rows"
                        )
                        block_index += 1
                    buf = trailing
                    if complete:
                        done_marker = True
                        complete_seen = True
                        effective_quiet = min(effective_quiet, 2.0)
                        break
                continue
            if raw and last_rx is not None and (time.monotonic() - last_rx) >= effective_quiet:
                break
    finally:
        writer.close()
    return bytes(raw), block_index, complete_seen


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


def _run_get_wavelengths(
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
    parsed = _handle_response(label, raw, log=log, parse_read=False)
    values = _parse_wavelength_table(parsed.data)
    if values:
        formatted = ", ".join(str(value) for value in values)
        print(f"{label}-values: {formatted}")
        if log:
            log.write(f"{label}-values {formatted}\n")
    time.sleep(0.2)


def _run_read_plate(
    fd: int,
    label: str,
    payload: bytes,
    timeout: float,
    quiet: float,
    log,
    *,
    decode: bool,
    wavelengths_per_interval: int,
    rows: int,
    cols: int,
    csv_path: str,
    incremental: bool,
) -> dict:
    _log_tx(log, label, payload)
    os.write(fd, payload)
    use_incremental = incremental and decode and bool(csv_path)
    if use_incremental:
        raw, block_count, complete_seen = _read_plate_streaming(
            fd,
            overall_timeout=timeout,
            quiet_timeout=quiet,
            wavelengths_per_interval=wavelengths_per_interval,
            rows=rows,
            cols=cols,
            csv_path=csv_path,
            label=label,
        )
        _handle_response(label, raw, log=log, parse_read=False)
        if csv_path:
            print(f"{label}-csv: {csv_path}")
        intervals = 0
        if block_count:
            intervals = (block_count + max(1, wavelengths_per_interval) - 1) // max(
                1, wavelengths_per_interval
            )
        print(
            f"{label}-intervals: {intervals} blocks={block_count} complete={complete_seen}"
        )
        summary = {"intervals": intervals, "blocks": block_count, "complete": complete_seen}
    else:
        raw = _read_response_with_continuation(
            fd, overall_timeout=timeout, quiet_timeout=quiet
        )
        parsed = _handle_response(label, raw, log=log, parse_read=True)
        if decode:
            rows_out = _decode_read_plate_payload(
                parsed.data,
                wavelengths_per_interval=wavelengths_per_interval,
                rows=rows,
                cols=cols,
            )
            if rows_out:
                if csv_path:
                    _write_read_plate_csv(rows_out, csv_path)
                    print(f"{label}-csv: {csv_path}")
                else:
                    print(
                        f"{label}-decode: rows={rows} cols={cols} "
                        f"intervals={rows_out[-1]['interval']}"
                    )
        intervals, blocks, complete = _summarize_read_plate(
            parsed.data, wavelengths_per_interval=wavelengths_per_interval
        )
        summary = {"intervals": intervals, "blocks": blocks, "complete": complete}
    time.sleep(0.2)
    return summary


def _run_read_wells(
    fd: int,
    label: str,
    payload: bytes,
    timeout: float,
    quiet: float,
    log,
    *,
    decode: bool,
    wavelengths_per_interval: int,
    csv_path: str,
    well_labels: list[str],
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
    parsed = _handle_response(label, raw, log=log, parse_read=True)
    if decode:
        rows = _decode_read_wells_payload(
            parsed.data,
            wavelengths_per_interval=wavelengths_per_interval,
            well_labels=well_labels,
        )
        if rows:
            if wavelengths_per_interval == 1 and len(rows) > 8:
                print(
                    f"{label}-decode: multiple blocks detected; consider "
                    f"--wavelengths-per-interval N to group intervals."
                )
            current_interval = None
            current_wavelength = None
            for row in rows:
                if (row["interval"], row["wavelength_index"]) != (
                    current_interval,
                    current_wavelength,
                ):
                    current_interval = row["interval"]
                    current_wavelength = row["wavelength_index"]
                    print(
                        f"{label}-interval {current_interval} wavelength {current_wavelength}:"
                    )
                value = "*****" if row["value"] is None else f"{row['value']:.3f}"
                print(f"  {row['well_label']}={value}")
            if csv_path:
                _write_read_wells_csv(rows, csv_path)
                print(f"{label}-csv: {csv_path}")
    time.sleep(0.2)


def _run_set_assay(
    fd: int,
    label: str,
    payload: bytes,
    timeout: float,
    quiet: float,
    log,
) -> None:
    _log_tx(log, f"{label}-cmd", b"V")
    os.write(fd, b"V")
    raw = core.read_response(fd, overall_timeout=min(1.0, timeout), quiet_timeout=0.2)
    ack = _handle_response(f"{label}-cmd", raw, log=log, parse_read=False)
    if not ack.ack:
        print(f"{label}: no ACK for command, aborting.")
        return
    _log_tx(log, f"{label}-payload", payload)
    os.write(fd, payload)
    raw = _read_response_with_continuation(
        fd, overall_timeout=timeout, quiet_timeout=quiet
    )
    _handle_response(label, raw, log=log, parse_read=False)
    time.sleep(0.2)


def _run_commands(
    fd: int,
    commands: list[tuple[str, bytes]],
    *,
    timeout: float,
    quiet: float,
    log,
    read_wells_opts: dict | None,
    read_plate_opts: dict | None,
) -> None:
    for label, payload in commands:
        if label == "read-plate":
            opts = read_plate_opts or {}
            _run_read_plate(fd, label, payload, timeout, quiet, log, **opts)
            continue
        if label == "read-wells":
            opts = read_wells_opts or {}
            _run_read_wells(fd, label, payload, timeout, quiet, log, **opts)
            continue
        if label == "get-wavelengths":
            _run_get_wavelengths(fd, label, payload, timeout, quiet, log)
            continue
        if label == "set-assay":
        _run_set_assay(fd, label, payload, timeout, quiet, log)
        continue
    _run_simple_command(fd, label, payload, timeout, quiet, log)


def _run_validate_short_run(
    fd: int,
    *,
    assay_args: argparse.Namespace,
    restore_args: argparse.Namespace | None,
    timeout: float,
    quiet: float,
    log,
    read_plate_opts: dict,
) -> bool:
    assay_payload = _build_assay_definition(assay_args)
    _run_set_assay(fd, "set-assay-validate", assay_payload, timeout, quiet, log)
    summary = _run_read_plate(fd, "read-plate", b"S", timeout, quiet, log, **read_plate_opts)
    expected = _expected_intervals(assay_args)
    ok = True
    if expected is not None and summary["intervals"] != expected:
        print(
            f"validate-short-run: expected {expected} intervals, got {summary['intervals']}"
        )
        ok = False
    if expected is not None and not summary["complete"]:
        print("validate-short-run: response blocks incomplete (missing terminator)")
        ok = False
    if restore_args is not None:
        restore_payload = _build_assay_definition(restore_args)
        _run_set_assay(fd, "set-assay-restore", restore_payload, timeout, quiet, log)
    if ok:
        print("validate-short-run: ok")
    return ok


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
        "--confirm-run",
        action="store_true",
        help="Shortcut for confirm-write/movement/read/assay.",
    )
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
    parser.add_argument(
        "--confirm-assay",
        action="store_true",
        help="Required for assay definition writes (set-assay).",
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
    read_plate = sub.add_parser("read-plate", help="Read plate ('S') with current assay definition.")
    read_plate.add_argument(
        "--decode",
        action="store_true",
        help="Decode read data into numeric values and print a summary.",
    )
    read_plate.add_argument(
        "--wavelengths-per-interval",
        type=int,
        default=1,
        help="Number of wavelengths per kinetic interval (for grouping).",
    )
    read_plate.add_argument(
        "--rows",
        type=int,
        default=8,
        help="Number of rows to decode (default 8 for 96-well plate).",
    )
    read_plate.add_argument(
        "--cols",
        type=int,
        default=12,
        help="Number of columns to decode (default 12 for 96-well plate).",
    )
    read_plate.add_argument(
        "--csv",
        default="",
        help="Write decoded plate values to a CSV file.",
    )
    read_plate.add_argument(
        "--incremental",
        action="store_true",
        help="Append decoded rows to CSV as intervals arrive.",
    )
    run_ecoplate = sub.add_parser(
        "run-ecoplate",
        help="Set an assay profile and run read-plate (defaults to ECO590).",
    )
    run_ecoplate.add_argument(
        "--profile",
        default="ECO590",
        help="Assay profile name (default ECO590).",
    )
    run_ecoplate.add_argument(
        "--profile-file",
        default="",
        help="Path to assay profile JSON (defaults to tools/elx808/assay_profiles.json).",
    )
    run_ecoplate.add_argument(
        "--wavelengths-per-interval",
        type=int,
        default=1,
        help="Number of wavelengths per kinetic interval (for grouping).",
    )
    run_ecoplate.add_argument(
        "--rows",
        type=int,
        default=8,
        help="Number of rows to decode (default 8 for 96-well plate).",
    )
    run_ecoplate.add_argument(
        "--cols",
        type=int,
        default=12,
        help="Number of columns to decode (default 12 for 96-well plate).",
    )
    run_ecoplate.add_argument(
        "--csv",
        default="/tmp/elx808-ecoplate.csv",
        help="Write decoded plate values to a CSV file.",
    )
    validate_short = sub.add_parser(
        "validate-short-run",
        help="Run a short assay profile and validate interval capture.",
    )
    validate_short.add_argument(
        "--profile",
        default="ECO60",
        help="Short-run assay profile name (default ECO60).",
    )
    validate_short.add_argument(
        "--restore-profile",
        default="ECO590",
        help="Assay profile to restore after validation (default ECO590).",
    )
    validate_short.add_argument(
        "--no-restore",
        action="store_true",
        help="Skip restoring the assay profile after validation.",
    )
    validate_short.add_argument(
        "--profile-file",
        default="",
        help="Path to assay profile JSON (defaults to tools/elx808/assay_profiles.json).",
    )
    validate_short.add_argument(
        "--wavelengths-per-interval",
        type=int,
        default=1,
        help="Number of wavelengths per kinetic interval (for grouping).",
    )
    validate_short.add_argument(
        "--rows",
        type=int,
        default=8,
        help="Number of rows to decode (default 8 for 96-well plate).",
    )
    validate_short.add_argument(
        "--cols",
        type=int,
        default=12,
        help="Number of columns to decode (default 12 for 96-well plate).",
    )
    validate_short.add_argument(
        "--csv",
        default="/tmp/elx808-validate.csv",
        help="Write decoded plate values to a CSV file.",
    )
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
    read_wells.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the encoded payload and exit without talking to the reader.",
    )
    read_wells.add_argument(
        "--decode",
        action="store_true",
        help="Decode read data into numeric values and print a summary.",
    )
    read_wells.add_argument(
        "--wavelengths-per-interval",
        type=int,
        default=1,
        help="Number of wavelengths per kinetic interval (for grouping).",
    )
    read_wells.add_argument(
        "--csv",
        default="",
        help="Write decoded read-wells values to a CSV file.",
    )
    sub.add_parser("get-wavelengths", help="Get wavelength table ('W').")
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
    set_assay = sub.add_parser(
        "set-assay",
        help="Download an assay definition table ('V') to the reader.",
    )
    set_assay.add_argument("--assay-name", default="", help="Assay name (max 6 ASCII chars).")
    set_assay.add_argument(
        "--profile",
        default="",
        help="Load assay settings from a named profile.",
    )
    set_assay.add_argument(
        "--profile-file",
        default="",
        help="Path to assay profile JSON (defaults to tools/elx808/assay_profiles.json).",
    )
    set_assay.add_argument(
        "--measurement-wavelength",
        type=int,
        default=None,
        help="Measurement wavelength (0 or 340-900). Required unless --wavelength is used.",
    )
    set_assay.add_argument(
        "--reference-wavelength",
        type=int,
        default=0,
        help="Reference wavelength (0 or 340-900).",
    )
    set_assay.add_argument(
        "--wavelength",
        action="append",
        type=int,
        default=[],
        help="Multi-wavelength list (use up to 6 entries).",
    )
    set_assay.add_argument(
        "--read-type",
        choices=["endpoint", "kinetic", "scan1d"],
        default="endpoint",
        help="Read type: endpoint, kinetic, or 1D scan.",
    )
    set_assay.add_argument(
        "--subtraction",
        choices=["none", "dual"],
        default="none",
        help="Dual-wavelength subtraction mode.",
    )
    set_assay.add_argument("--scan-points", type=int, default=1, help="1D scan points (odd 1-31).")
    set_assay.add_argument("--kinetic-interval", type=int, default=None, help="Kinetic interval seconds.")
    set_assay.add_argument(
        "--kinetic-read-count",
        type=int,
        default=None,
        help="Kinetic read count (2-9999).",
    )
    set_assay.add_argument(
        "--use-total-kinetic-time",
        action="store_true",
        help="Use total kinetic read time instead of read count.",
    )
    set_assay.add_argument(
        "--total-kinetic-read-time",
        type=int,
        default=None,
        help="Total kinetic read time in minutes (1-9999).",
    )
    set_assay.add_argument("--shake", action="store_true", help="Enable shaking.")
    set_assay.add_argument(
        "--shake-every-read",
        action="store_true",
        help="Shake before every read (else only before first).",
    )
    set_assay.add_argument(
        "--shake-continuous",
        action="store_true",
        help="Use continuous shake (else timed).",
    )
    set_assay.add_argument("--shake-time", type=int, default=0, help="Shake time seconds (0-999).")
    set_assay.add_argument(
        "--shake-speed",
        type=int,
        default=0,
        choices=[0, 1, 2, 3],
        help="Shake speed: 0 slow, 1 med, 2 fast, 3 variable.",
    )
    set_assay.add_argument(
        "--delay-seconds",
        type=int,
        default=0,
        help="Delay before first read in seconds (0-999).",
    )
    set_assay.add_argument(
        "--delay-enabled",
        type=int,
        choices=[0, 1],
        default=None,
        help="Override delay enable (1 yes, 0 no). Defaults to enabled if delay-seconds > 0.",
    )
    set_assay.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the encoded assay payload and exit without talking to the reader.",
    )

    args, unknown = parser.parse_known_args()
    provided_flags = {arg for arg in sys.argv if arg.startswith("--")}
    if args.confirm_run:
        args.confirm_write = True
        args.confirm_movement = True
        args.confirm_read = True
        args.confirm_assay = True
    if "--confirm-write" in unknown:
        args.confirm_write = True
    if "--confirm-movement" in unknown:
        args.confirm_movement = True
    if "--confirm-read" in unknown:
        args.confirm_read = True
    if "--confirm-assay" in unknown:
        args.confirm_assay = True
    unknown = [
        item
        for item in unknown
        if item
        not in ("--confirm-write", "--confirm-movement", "--confirm-read", "--confirm-assay")
    ]
    if unknown:
        parser.error(f"unrecognized arguments: {' '.join(unknown)}")

    if args.command == "set-assay" and args.profile:
        profile_path = args.profile_file
        if not profile_path:
            profile_path = os.path.join(os.path.dirname(__file__), "assay_profiles.json")
        try:
            _apply_assay_profile(
                args,
                profile_name=args.profile,
                profile_file=profile_path,
                provided_flags=provided_flags,
            )
        except ValueError as exc:
            parser.error(str(exc))
    if args.command == "set-assay" and not args.assay_name:
        parser.error("--assay-name is required unless --profile provides one.")
    commands: list[tuple[str, bytes]] = []
    needs_write = False
    needs_movement = False
    needs_read = False
    needs_assay = False
    validation_plan: dict | None = None
    try:
        if args.command == "sequence":
            if not args.skip_set_status:
                label = f"set-status-{args.mode}"
                payload = b"n1" if args.mode == "elx" else b"n0"
                commands.append((label, payload))
                needs_write = True
            for cmd_label in ("status", "version"):
                label, payload, write, movement, read, assay = _build_command(
                    argparse.Namespace(command=cmd_label)
                )
                commands.append((label, payload))
                needs_write = needs_write or write
                needs_movement = needs_movement or movement
                needs_read = needs_read or read
                needs_assay = needs_assay or assay
        elif args.command == "run-ecoplate":
            profile_path = args.profile_file
            if not profile_path:
                profile_path = os.path.join(os.path.dirname(__file__), "assay_profiles.json")
            try:
                assay_args = _load_assay_from_profile(args.profile, profile_path)
            except ValueError as exc:
                parser.error(str(exc))
            payload = _build_assay_definition(assay_args)
            commands.append(("set-assay", payload))
            commands.append(("read-plate", b"S"))
            needs_write = True
            needs_movement = True
            needs_read = True
            needs_assay = True
            if not _flag_present(provided_flags, "--timeout"):
                duration = _estimate_kinetic_duration_seconds(assay_args)
                if duration:
                    interval = assay_args.kinetic_interval or 0
                    buffer = max(600.0, float(interval) + 60.0)
                    args.timeout = max(args.timeout, duration + buffer)
            if not _flag_present(provided_flags, "--quiet"):
                interval = assay_args.kinetic_interval or 0
                if interval:
                    args.quiet = max(args.quiet, float(interval) + 60.0)
        elif args.command == "validate-short-run":
            profile_path = args.profile_file
            if not profile_path:
                profile_path = os.path.join(os.path.dirname(__file__), "assay_profiles.json")
            try:
                assay_args = _load_assay_from_profile(args.profile, profile_path)
                restore_args = None
                if not args.no_restore:
                    restore_args = _load_assay_from_profile(args.restore_profile, profile_path)
            except ValueError as exc:
                parser.error(str(exc))
            validation_plan = {
                "assay_args": assay_args,
                "restore_args": restore_args,
            }
            needs_write = True
            needs_movement = True
            needs_read = True
            needs_assay = True
            if not _flag_present(provided_flags, "--timeout"):
                duration = _estimate_kinetic_duration_seconds(assay_args)
                if duration:
                    interval = assay_args.kinetic_interval or 0
                    buffer = max(600.0, float(interval) + 60.0)
                    args.timeout = max(args.timeout, duration + buffer)
            if not _flag_present(provided_flags, "--quiet"):
                interval = assay_args.kinetic_interval or 0
                if interval:
                    args.quiet = max(args.quiet, float(interval) + 60.0)
        else:
            label, payload, needs_write, needs_movement, needs_read, needs_assay = _build_command(args)
            commands = [(label, payload)]
    except ValueError as exc:
        parser.error(str(exc))

    if args.command == "read-wells" and getattr(args, "dry_run", False):
        packet = payload + bytes([core.ETX])
        print(f"read-wells payload_hex={core.hexdump(payload)} payload_ascii={core.ascii_repr(payload)}")
        print(f"read-wells packet_hex={core.hexdump(packet)} packet_ascii={core.ascii_repr(packet)}")
        print("read-wells dry-run complete (no serial I/O).")
        return 0

    if args.command == "set-assay" and getattr(args, "dry_run", False):
        print(f"set-assay payload_len={len(payload)}")
        print(f"set-assay payload_hex={core.hexdump(payload)}")
        print(f"set-assay payload_ascii={core.ascii_repr(payload)}")
        print("set-assay dry-run complete (no serial I/O).")
        return 0

    confirmation = _require_confirmation(
        args, needs_write, needs_movement, needs_read, needs_assay
    )
    if confirmation:
        return confirmation

    read_wells_opts = None
    read_plate_opts = None
    if args.command == "read-wells":
        if args.payload_hex or args.payload_file:
            well_labels = [f"W{i + 1}" for i in range(8)]
        else:
            well_labels = list(args.well)
            for idx in range(len(well_labels) + 1, 9):
                well_labels.append(f"unused{idx}")
        read_wells_opts = {
            "decode": bool(args.decode or args.csv),
            "wavelengths_per_interval": args.wavelengths_per_interval,
            "csv_path": args.csv,
            "well_labels": well_labels,
        }
    if args.command in ("read-plate", "run-ecoplate", "validate-short-run"):
        decode = True if args.command in ("run-ecoplate", "validate-short-run") else bool(
            args.decode or args.csv
        )
        incremental = False
        if args.command == "run-ecoplate":
            incremental = True
        if args.command == "validate-short-run":
            incremental = True
        elif args.command == "read-plate":
            incremental = bool(getattr(args, "incremental", False))
        read_plate_opts = {
            "decode": decode,
            "wavelengths_per_interval": args.wavelengths_per_interval,
            "rows": args.rows,
            "cols": args.cols,
            "csv_path": args.csv,
            "incremental": incremental,
        }

    log_path = args.log
    log = open(log_path, "w", encoding="utf-8") if log_path else None
    if args.command == "run-ecoplate":
        print(
            f"run-ecoplate: profile={args.profile} timeout={args.timeout:.0f}s "
            f"quiet={args.quiet:.0f}s csv={args.csv}"
        )
    if args.command == "validate-short-run":
        print(
            f"validate-short-run: profile={args.profile} timeout={args.timeout:.0f}s "
            f"quiet={args.quiet:.0f}s csv={args.csv}"
        )

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

        if validation_plan is not None:
            ok = _run_validate_short_run(
                fd,
                assay_args=validation_plan["assay_args"],
                restore_args=validation_plan["restore_args"],
                timeout=args.timeout,
                quiet=args.quiet,
                log=log,
                read_plate_opts=read_plate_opts or {},
            )
            if not ok:
                return 1
        else:
            _run_commands(
                fd,
                commands,
                timeout=args.timeout,
                quiet=args.quiet,
                log=log,
                read_wells_opts=read_wells_opts,
                read_plate_opts=read_plate_opts,
            )
    finally:
        if log:
            log.close()
        os.close(fd)

    if log_path:
        print(f"Wrote log: {log_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
