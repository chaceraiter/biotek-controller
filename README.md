# biotek-controller

This repo is a research-first effort to communicate with a legacy BioTek ELx808 microplate reader over RS-232 and eventually build modern control + data retrieval software.

## First-time setup and testing (macOS / Unix)

This section is written so someone can clone the repo and attempt a safe “first contact” with an ELx808 that is already plugged into a Mac via a USB-to-serial adapter (optionally through a USB→USB‑C dongle).

1) Clone:
```bash
git clone https://github.com/chaceraiter/biotek-controller.git
cd biotek-controller
```

2) Confirm prerequisites:
- Hardware: BioTek ELx808 connected to the **DB25 “serial”** port (not the “parallel” port).
- Adapter: USB-to-serial that is **RS-232 voltage level** (not TTL UART).
- Instrument settings: ELx808 serial framing is **8 data bits, no parity, 2 stop bits (8N2)**.
  - Baud is selectable; this repo currently assumes the instrument is set to **9600**.

Reference docs in this repo:
- Serial pinout: `research/elx808/ports-and-pinouts.md`
- Serial settings: `research/elx808/serial-settings.md`

3) Find the serial device on the Mac:
```bash
ls -1 /dev/cu.* /dev/tty.* 2>/dev/null | grep -Ei 'usb|serial|usbserial|usbmodem' || true
```

Pick the likely device path (prefer `/dev/cu.*` on macOS). Examples: `/dev/cu.usbserial-XXXX`, `/dev/cu.usbmodemXXXX`.

4) Capture traffic (safe / minimal writes)

Try no flow control first:
```bash
python3 tools/elx808/serial_capture.py \
  --port /dev/cu.YOURDEVICE \
  --baud 9600 \
  --stopbits 2 \
  --parity N \
  --flow none \
  --send CRLF \
  --duration 15
```

If you see nothing, retry with RTS/CTS hardware flow control:
```bash
python3 tools/elx808/serial_capture.py \
  --port /dev/cu.YOURDEVICE \
  --baud 9600 \
  --stopbits 2 \
  --parity N \
  --flow rtscts \
  --send CRLF \
  --duration 15
```

Tip: run the capture while power-cycling the ELx808 to see if it emits a boot banner.

5) Share results
- The script prints the log file path it wrote.
- Paste the `rx ...` lines (or attach the whole log) so we can infer the on-wire protocol.

## Safety notes
- Do not attempt firmware/basecode updates or assay downloads until the protocol is understood.
- Early work should stick to passive listening and minimal “poke” bytes (CR/LF/`?`).

## Where to read next
- Serial pinout and implications: `research/elx808/ports-and-pinouts.md`
- Serial settings references: `research/elx808/serial-settings.md`
- Bring-up checklist: `research/elx808/serial-bringup.md`
- macOS host notes: `research/elx808/host-setup-macos.md`
- Tool usage: `tools/elx808/README.md`
- Expanded checklist: `docs/testing-first-contact.md`
- Troubleshooting: `docs/troubleshooting.md`

## Troubleshooting (common)
- No bytes received:
  - Try `--flow rtscts`.
  - Confirm instrument baud matches `--baud` (ELx808 supports 1200/2400/9600; framing is 8N2).
  - Consider that you may need a **DB25 null-modem/cross-over** (depends on whether the USB adapter is DTE vs DCE).
- Garbage characters:
  - Baud is wrong (try 2400 8N2 as a sanity check).
- “Resource busy” / can’t open the port:
  - Close other serial apps (screen/minicom, etc.) and retry.
