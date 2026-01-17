from __future__ import annotations

from dataclasses import dataclass
import os
import select
import time

ACK = 0x06
NAK = 0x15
RS = 0x1E
ETX = 0x03
CTRL_Z = 0x1A
DLE = 0x10


def hexdump(data: bytes) -> str:
    return " ".join(f"{b:02x}" for b in data)


def ascii_repr(data: bytes) -> str:
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


@dataclass(frozen=True)
class Status:
    mode: str
    code: str
    raw: bytes


def parse_status(candidate: bytes) -> Status | None:
    if len(candidate) != 5 or candidate[-1] != ETX:
        return None
    if candidate[0] == RS:
        code = candidate[1:4].decode("ascii", errors="replace")
        return Status(mode="312", code=code, raw=candidate)
    if all(_is_ascii_hex(b) for b in candidate[:4]):
        code = candidate[:4].decode("ascii", errors="replace")
        return Status(mode="ELx", code=code, raw=candidate)
    return None


def split_leading_status(payload: bytes) -> tuple[Status | None, bytes]:
    if len(payload) < 5:
        return None, payload
    candidate = payload[:5]
    parsed = parse_status(candidate)
    if parsed:
        return parsed, payload[5:]
    return None, payload


def split_status(payload: bytes) -> tuple[bytes, bytes, Status | None]:
    etx_idx = payload.rfind(bytes([ETX]))
    if etx_idx < 4:
        return payload, b"", None
    candidate = payload[etx_idx - 4 : etx_idx + 1]
    parsed = parse_status(candidate)
    if parsed is None:
        return payload, b"", None
    data = payload[: etx_idx - 4]
    return data, candidate, parsed


@dataclass(frozen=True)
class Response:
    ack: bool
    nak: bool
    data: bytes
    status: bytes
    status_parsed: Status | None
    raw: bytes


def parse_response(raw: bytes) -> Response:
    ack = raw.startswith(bytes([ACK]))
    nak = raw.startswith(bytes([NAK]))
    payload = raw[1:] if (ack or nak) else raw
    data, status_raw, status_parsed = split_status(payload)
    return Response(
        ack=ack,
        nak=nak,
        data=data,
        status=status_raw,
        status_parsed=status_parsed,
        raw=raw,
    )


@dataclass(frozen=True)
class ElxFrame:
    raw: bytes
    start_idx: int
    end_idx: int
    payload: bytes
    checksum: bytes
    terminator: int | None
    trailing: bytes
    complete: bool


def parse_elx_frame(data: bytes) -> ElxFrame | None:
    start = data.find(bytes([RS]))
    if start == -1:
        return None
    end = data.find(bytes([ETX]), start + 1)
    if end == -1:
        payload = data[start + 1 :]
        return ElxFrame(
            raw=data[start:],
            start_idx=start,
            end_idx=-1,
            payload=payload,
            checksum=b"",
            terminator=None,
            trailing=b"",
            complete=False,
        )
    payload = data[start + 1 : end]
    remainder = data[end + 1 :]
    checksum = b""
    terminator = None
    trailing = b""
    complete = True
    if remainder:
        if CTRL_Z in remainder:
            term_idx = remainder.index(bytes([CTRL_Z]))
            checksum = remainder[:term_idx]
            terminator = CTRL_Z
            trailing = remainder[term_idx + 1 :]
        else:
            checksum = remainder
            complete = False
    return ElxFrame(
        raw=data[start : end + 1] + remainder,
        start_idx=start,
        end_idx=end,
        payload=payload,
        checksum=checksum,
        terminator=terminator,
        trailing=trailing,
        complete=complete,
    )


@dataclass(frozen=True)
class ElxWavelengthBlock:
    payload: bytes
    checksum: int


def parse_elx_wavelength_blocks(data: bytes) -> tuple[list[ElxWavelengthBlock], bool, bytes]:
    blocks: list[ElxWavelengthBlock] = []
    idx = 0
    while True:
        term_idx = data.find(bytes([CTRL_Z]), idx)
        if term_idx == -1:
            return blocks, False, data[idx:]
        if term_idx + 1 >= len(data):
            return blocks, False, data[idx:]
        payload = data[idx:term_idx]
        checksum = data[term_idx + 1]
        blocks.append(ElxWavelengthBlock(payload=payload, checksum=checksum))
        idx = term_idx + 2
        if idx < len(data) and data[idx] == CTRL_Z:
            return blocks, True, data[idx + 1 :]
        if idx >= len(data):
            return blocks, False, b""


def format_response_summary(parsed: Response) -> str:
    status_tag = "none"
    if parsed.status_parsed:
        status_tag = f"{parsed.status_parsed.mode}:{parsed.status_parsed.code}"
    return (
        f"ack={parsed.ack} nak={parsed.nak} data_hex={hexdump(parsed.data)} "
        f"status_hex={hexdump(parsed.status)} status={status_tag}"
    )


def format_frame_summary(frame: ElxFrame) -> str:
    term = f"{frame.terminator:02x}" if frame.terminator is not None else "none"
    return (
        f"frame_start={frame.start_idx} frame_end={frame.end_idx} complete={frame.complete} "
        f"payload_hex={hexdump(frame.payload)} checksum_hex={hexdump(frame.checksum)} "
        f"terminator_hex={term} trailing_hex={hexdump(frame.trailing)}"
    )


def log_block(log, label: str, raw: bytes, parsed: Response) -> None:
    log.write(f"{label} raw_hex={hexdump(raw)} raw_ascii={ascii_repr(raw)}\n")
    log.write(f"{label} {format_response_summary(parsed)}\n")
