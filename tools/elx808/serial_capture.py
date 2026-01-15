#!/usr/bin/env python3
import argparse
import datetime as _dt
import os
import select
import sys
import termios
import time
import tty


def _baud_to_termios(baud: int) -> int:
    name = f"B{baud}"
    value = getattr(termios, name, None)
    if value is None:
        raise ValueError(f"Unsupported baud rate for this platform: {baud} (no termios.{name})")
    return value


def _set_modem_line(fd: int, line: str, enabled: bool) -> None:
    if not hasattr(termios, "TIOCMGET") or not hasattr(termios, "TIOCMSET"):
        return

    line_bit = getattr(termios, f"TIOCM_{line}", None)
    if line_bit is None:
        return

    import fcntl
    import struct

    buf = array = struct.pack("I", 0)
    out = fcntl.ioctl(fd, termios.TIOCMGET, buf)
    (state,) = struct.unpack("I", out)

    if enabled:
        state |= line_bit
    else:
        state &= ~line_bit

    fcntl.ioctl(fd, termios.TIOCMSET, struct.pack("I", state))


def configure_serial(
    fd: int,
    *,
    baud: int,
    databits: int,
    parity: str,
    stopbits: int,
    flow: str,
) -> None:
    tty.setraw(fd)
    attrs = termios.tcgetattr(fd)

    baud_const = _baud_to_termios(baud)
    termios.cfsetispeed(attrs, baud_const)
    termios.cfsetospeed(attrs, baud_const)

    cflag = attrs[2]
    cflag &= ~termios.CSIZE

    if databits == 8:
        cflag |= termios.CS8
    elif databits == 7:
        cflag |= termios.CS7
    else:
        raise ValueError("Only 7 or 8 databits are supported")

    parity = parity.upper()
    if parity == "N":
        cflag &= ~termios.PARENB
    elif parity == "E":
        cflag |= termios.PARENB
        cflag &= ~termios.PARODD
    elif parity == "O":
        cflag |= termios.PARENB
        cflag |= termios.PARODD
    else:
        raise ValueError("Parity must be N, E, or O")

    if stopbits == 2:
        cflag |= termios.CSTOPB
    elif stopbits == 1:
        cflag &= ~termios.CSTOPB
    else:
        raise ValueError("Stopbits must be 1 or 2")

    if hasattr(termios, "CRTSCTS"):
        if flow == "rtscts":
            cflag |= termios.CRTSCTS
        else:
            cflag &= ~termios.CRTSCTS

    attrs[2] = cflag

    iflag = attrs[0]
    if flow == "xonxoff":
        iflag |= termios.IXON | termios.IXOFF
    else:
        iflag &= ~(termios.IXON | termios.IXOFF | termios.IXANY)
    attrs[0] = iflag

    # Non-blocking reads; we use select() for timing.
    cc = attrs[6]
    cc[termios.VMIN] = 0
    cc[termios.VTIME] = 0

    termios.tcsetattr(fd, termios.TCSANOW, attrs)


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
        elif b == 0x09:
            out.append("\\t")
        else:
            out.append(".")
    return "".join(out)


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
    return value.encode("utf-8", errors="replace")


def main() -> int:
    parser = argparse.ArgumentParser(description="Capture/send bytes over a serial port (std-lib termios).")
    parser.add_argument("--port", required=True, help="Serial device path (prefer /dev/cu.* on macOS).")
    parser.add_argument("--baud", type=int, default=9600)
    parser.add_argument("--databits", type=int, default=8, choices=[7, 8])
    parser.add_argument("--parity", default="N", choices=["N", "E", "O"])
    parser.add_argument("--stopbits", type=int, default=2, choices=[1, 2])
    parser.add_argument("--flow", default="none", choices=["none", "rtscts", "xonxoff"])
    parser.add_argument("--send", action="append", default=[], help="Send token: CR, LF, CRLF, HEX:.., or text.")
    parser.add_argument("--duration", type=float, default=0.0, help="Seconds to run; 0 means until Ctrl-C.")
    parser.add_argument("--log", default="", help="Log file path (defaults to timestamped file).")
    parser.add_argument("--set-dtr", type=int, choices=[0, 1], default=None, help="Best-effort DTR line set.")
    parser.add_argument("--set-rts", type=int, choices=[0, 1], default=None, help="Best-effort RTS line set.")
    args = parser.parse_args()

    log_path = args.log or f"elx808-serial-{_dt.datetime.now().strftime('%Y%m%d-%H%M%S')}.log"

    fd = os.open(args.port, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
    try:
        configure_serial(
            fd,
            baud=args.baud,
            databits=args.databits,
            parity=args.parity,
            stopbits=args.stopbits,
            flow=args.flow,
        )

        if args.set_dtr is not None:
            _set_modem_line(fd, "DTR", bool(args.set_dtr))
        if args.set_rts is not None:
            _set_modem_line(fd, "RTS", bool(args.set_rts))

        with open(log_path, "w", encoding="utf-8") as log:
            log.write(f"port={args.port}\n")
            log.write(f"baud={args.baud} databits={args.databits} parity={args.parity} stopbits={args.stopbits} flow={args.flow}\n")
            log.write(f"start={_dt.datetime.now().isoformat()}\n")
            log.flush()

            for item in args.send:
                payload = _parse_send_arg(item)
                os.write(fd, payload)
                log.write(f"tx {time.time():.6f} hex={_hexdump(payload)} ascii={_ascii_repr(payload)}\n")
                log.flush()

            start = time.monotonic()
            while True:
                if args.duration and (time.monotonic() - start) >= args.duration:
                    break

                r, _, _ = select.select([fd], [], [], 0.25)
                if not r:
                    continue

                data = os.read(fd, 4096)
                if not data:
                    continue

                log.write(f"rx {time.time():.6f} hex={_hexdump(data)} ascii={_ascii_repr(data)}\n")
                log.flush()

    finally:
        os.close(fd)

    print(f"Wrote log: {log_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

