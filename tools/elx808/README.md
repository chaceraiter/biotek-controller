# ELx808 tooling

## `serial_capture.py`

Minimal serial capture/send tool using only the Python standard library (no `pyserial` dependency).

### Find the port

macOS:
```bash
ls -1 /dev/cu.* /dev/tty.* 2>/dev/null
```

Prefer `/dev/cu.*` for initiating outbound connections.

Linux:
```bash
ls -1 /dev/ttyUSB* /dev/ttyACM* 2>/dev/null
```

### Examples (macOS)

```bash
python3 tools/elx808/serial_capture.py --port /dev/cu.usbserial-XXXX --baud 9600 --stopbits 2 --parity N --duration 15
python3 tools/elx808/serial_capture.py --port /dev/cu.usbserial-XXXX --baud 9600 --stopbits 2 --parity N --send CRLF --send "?\\r" --duration 10
```

Tip: try both `--flow none` and `--flow rtscts` if you see no responses.

### Logging

- By default, logs are written to the current directory as `elx808-serial-YYYYMMDD-HHMMSS.log`.
- Use `--log` to write to a specific path:

```bash
mkdir -p logs
python3 tools/elx808/serial_capture.py --port /dev/cu.usbserial-XXXX --baud 9600 --stopbits 2 --parity N --flow none --duration 15 --log logs/first-contact.log
```

### What the log contains

Each transmit/receive line includes:
- Unix timestamp (seconds since epoch)
- `hex=`: raw bytes in hex
- `ascii=`: printable ASCII with `\r` and `\n` escaped

## `adapter_probe.py`

Best-effort USB-serial adapter probe. This script inspects USB descriptor
strings and known chipset hints, but it cannot verify electrical levels.
Always confirm RS-232 vs TTL by adapter labeling or measurement.

Example (macOS or Linux):
```bash
python3 tools/elx808/adapter_probe.py
```

Watch for new serial nodes while plugging in the adapter:
```bash
python3 tools/elx808/adapter_probe.py --watch 15
```

## `protocol_probe.py`

Safe-by-default protocol probe using Appendix B commands. By default it sends:
- `o` (Get Current Status)
- `e` (Get Basecode Version)

These should not move the instrument. Self-test (`*`) is only sent with explicit confirmation.

Example (status + version, log to file):
```bash
python3 tools/elx808/protocol_probe.py --port /dev/cu.usbserial-XXXX --log /tmp/elx808-probe.log
```

Force ELx status format before probing:
```bash
python3 tools/elx808/protocol_probe.py --port /dev/cu.usbserial-XXXX --set-status elx --log /tmp/elx808-probe.log
```

Self-test (movement):
```bash
python3 tools/elx808/protocol_probe.py --port /dev/cu.usbserial-XXXX --self-test --confirm-self-test --log /tmp/elx808-selftest.log
```

## `control_stack.py`

Minimal control stack (transport + protocol wrapper). Read-only commands are
safe by default; state-changing commands require explicit confirmation flags.

Status:
```bash
python3 tools/elx808/control_stack.py --port /dev/cu.usbserial-XXXX status
```

Version (log to file):
```bash
python3 tools/elx808/control_stack.py --port /dev/cu.usbserial-XXXX version --log /tmp/elx808-version.log
```

Set status format (state-changing):
```bash
python3 tools/elx808/control_stack.py --port /dev/cu.usbserial-XXXX set-status elx --confirm-write
```

Self-test (movement):
```bash
python3 tools/elx808/control_stack.py --port /dev/cu.usbserial-XXXX self-test --confirm-movement --log /tmp/elx808-selftest.log
```

Sequence (set status format, then status + version in one session):
```bash
python3 tools/elx808/control_stack.py --port /dev/cu.usbserial-XXXX sequence --confirm-write
```

Scaffolded read commands (movement + write + read gated):
```bash
python3 tools/elx808/control_stack.py --port /dev/cu.usbserial-XXXX read-plate --confirm-write --confirm-movement --confirm-read
python3 tools/elx808/control_stack.py --port /dev/cu.usbserial-XXXX read-wells --well A1 --well B2 --confirm-write --confirm-movement --confirm-read
```

Advanced: override the read-wells payload directly (33 bytes):
```bash
python3 tools/elx808/control_stack.py --port /dev/cu.usbserial-XXXX read-wells --payload-hex "01 01 01 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 30" --confirm-write --confirm-movement --confirm-read
```
