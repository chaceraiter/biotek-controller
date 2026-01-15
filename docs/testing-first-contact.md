# Testing “First Contact” with an ELx808 (macOS/Unix)

This doc expands the quickstart in `README.md` into a repeatable checklist for capturing the first useful serial transcript.

## Inputs you should record
- Host OS (macOS version or Linux distro).
- USB serial adapter model/chipset (if you know it).
- Whether you used a USB→USB‑C adapter/dongle.
- Whether you used any **null-modem/cross-over** adapter between host and instrument.
- Instrument baud setting (1200 / 2400 / 9600).

## 0) Confirm you’re on the serial port
The ELx808 has separate DB25 “serial” and “parallel” ports. Use the DB25 **serial** port.

## 1) Confirm serial settings
The ELx808 framing is fixed at **8N2** (8 data bits, no parity, 2 stop bits). Baud is selectable.

If you’re unsure what the instrument is set to, try 9600 first (common for PC control via KCjunior), then 2400.

## 2) Find the device node
macOS:
```bash
ls -1 /dev/cu.* /dev/tty.* 2>/dev/null
```

Prefer `/dev/cu.*` for initiating outbound connections.

Linux:
```bash
ls -1 /dev/ttyUSB* /dev/ttyACM* 2>/dev/null
```

## 3) Baseline capture (no writes)
Start a capture and power-cycle the instrument during the capture window:
```bash
python3 tools/elx808/serial_capture.py --port /dev/cu.YOURDEVICE --baud 9600 --stopbits 2 --parity N --flow none --duration 20
```

Repeat with RTS/CTS if needed:
```bash
python3 tools/elx808/serial_capture.py --port /dev/cu.YOURDEVICE --baud 9600 --stopbits 2 --parity N --flow rtscts --duration 20
```

## 4) Gentle “poke” capture
If the instrument doesn’t emit anything spontaneously, send minimal bytes:
```bash
python3 tools/elx808/serial_capture.py --port /dev/cu.YOURDEVICE --baud 9600 --stopbits 2 --parity N --flow none --send CR --send LF --send "?\r" --duration 10
```

## 5) If nothing works
Work through, in order:
- Verify baud (try 2400 8N2).
- Verify flow control (`--flow rtscts`).
- Verify cabling (you may need a DB25 null-modem/cross-over depending on your USB adapter).
- Verify the USB adapter is RS‑232 level (not TTL UART).

## 6) What to share back
- The first ~50 lines of the log (especially any `rx ...` lines).
- Any observation from the ELx808 UI (errors, “computer control” mode, etc.).
