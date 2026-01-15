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

