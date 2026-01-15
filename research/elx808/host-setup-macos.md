# BioTek ELx808 — Host Setup (macOS / Unix)

Goal: Use a modern Mac (optionally via a USB→USB‑C adapter) to talk to the ELx808 over RS‑232.

## Hardware
- ELx808 “serial” port: DB25 male on the instrument.
- Host: USB-to-RS232 adapter/cable, plus USB→USB‑C adapter if needed.

Important: confirm the USB adapter is **RS‑232 level** (not TTL UART).

## Find the serial device on macOS
Plug in the USB-serial adapter and run:

```bash
ls -1 /dev/cu.* /dev/tty.* 2>/dev/null | grep -Ei 'usb|wch|serial|usbserial|usbmodem' || true
```

Notes:
- Prefer `/dev/cu.*` for initiating outbound connections (it avoids waiting for modem control lines).
- `/dev/tty.*` is typically for incoming modem-style connections.

## Settings to use (from ELx808 docs)
- Baud: **9600** (your instrument is currently configured to 9600)
- Data bits: **8**
- Parity: **None**
- Stop bits: **2**

Shorthand: **9600 8N2**

## First contact
Use the script in `tools/elx808/serial_capture.py` to:
- listen while power-cycling the instrument,
- optionally send minimal “poke” bytes (CR/LF/?),
- log raw bytes for later protocol analysis.
