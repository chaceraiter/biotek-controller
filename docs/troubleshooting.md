# Troubleshooting ELx808 Serial Communication

This project is early-stage reverse engineering. If “first contact” fails, most issues are physical layer or settings mismatches.

## 1) Confirm you’re using RS‑232, not TTL UART
- Many “USB serial” boards expose 3.3V/5V TTL (TX/RX/GND). Those are **not** RS‑232.
- The ELx808 DB25 serial port is RS‑232; you need a USB-to-**RS‑232** adapter/cable.

## 2) Confirm you’re on the ELx808 “serial” port
The ELx808 has a separate DB25 “parallel” port. The DB25 **serial** port pinout is in `research/elx808/ports-and-pinouts.md`.

## 3) Confirm the framing: 8N2
Per the operator manual, the ELx808 uses:
- 8 data bits
- No parity
- 2 stop bits

If you use 8N1, you may see nothing or garbage.

## 4) Confirm baud: 9600 vs 2400
Baud is selectable on the instrument (commonly 1200/2400/9600). If you see garbage, try 2400 8N2.

## 5) Try flow control both ways
Some devices require hardware flow control; some adapters mis-handle it.
- Try `--flow none` and `--flow rtscts`.

## 6) Consider a null-modem / cross-over requirement
The ELx808 serial DB25 pinout matches the DB25 **DTE** convention (TX on 2, RX on 3).

Whether you need a null-modem depends on your USB adapter:
- If the adapter behaves like **DTE** (common), you need a **null-modem/cross-over** between host and ELx808.
- If the adapter behaves like **DCE**, straight-through is correct.

Practical approach: try both “as-is” and with a DB25 null-modem adapter.

## 7) Confirm exclusive access to the port
If you get “resource busy” errors:
- Close other serial apps (screen/minicom/etc.).
- Unplug/replug the USB adapter and retry.

## 8) What to share for debugging
Paste:
- Your chosen device path (`/dev/cu.*` or `/dev/ttyUSB*`).
- The exact command you ran.
- The resulting log’s `rx ...` lines (or the whole log file).

