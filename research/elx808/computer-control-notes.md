# BioTek ELx808 — Computer Control Notes (Appendix B Excerpt)

Source: `docs/op-man` (Appendix B: computer control protocol).

## Capabilities / behavior under computer control
- Supports defining and running computer-controlled **kinetic assays** using up to **three wavelengths** on the same microplate.
- When computer control is used:
  - the ELx808’s **onboard blanking** is suppressed
  - the ELx808’s **data reduction calculations** are suppressed
  - **raw data** is returned to the controlling software for evaluation
  - readings **higher than 3.000 OD** may be transmitted

## Software mentioned
- Bio-Tek **KCjunior** and **KC4** are referenced as controlling software packages at the time of the manual.
- User notes newer software ecosystem appears to be Agilent **Gen5** (not yet validated in-project).

## Next artifact needed
- The actual Appendix B protocol definition and command set pages (framing, checksums, request/response formats, error/status codes).

## Serial settings and cabling (from Appendix B + KCjunior/KC4 setup)
- RS-232C, fixed framing: 8 data bits, no parity, 2 stop bits (8N2).
- Baud rate is stored in NVM; supported: 1200 / 2400 / 9600 (default varies).
- RS-232 port is DTE: TX on pin 2, RX on pin 3. Host must be DCE or use a null-modem.
- KCjunior setup: 9600 8N2, EOT character left at default.
- If comms fail, manual advises checking for a null-modem and adding another if needed.

## Control characters
- ACK: 0x06
- NAK: 0x15
- RS: 0x1E
- ETX: 0x03
- DLE: 0x10
- CR/LF: 0x0D/0x0A
- CTRL-Z: 0x1A

## Command/response framing rules
- Commands are single ASCII characters, sometimes followed by argument bytes.
- On valid command receipt, reader returns ACK.
- If invalid characters are seen while waiting for a command, reader clears its input buffer and sends NAK (so leading noise can cause misses).
- For commands that return data, data is sent first, then a status string.

## Status string format
- Status string length: 5 bytes.
- Two formats: 312 mode vs ELx mode (select with `n`).
- In ELx status mode, any non-zero character indicates an error; read commands may include a final status string at end of data.
- `o` (Get Current Status) returns ELx status format and clears non-fatal errors unless a self-test is required.
- Empirical: sending `n1` (set status to ELx) before `o` and `e` yields ELx status `0000` suffixes; without it, `e` may return 312 status `000`.

## Useful commands (Appendix B)
- `*` Self-test: runs calibration/self-test, returns variable ASCII data then status.
- `o` Get current status: returns ELx status string and clears non-fatal errors.
- `e` Get basecode version: part number + " Version " + version code + status.
- `q` Quiet mode: `0` off, `1` on (suppresses beeping; use status to see errors).
- `n` Set status format: `0` 312, `1` ELx.
- `i` Include temperature response in read data: `0`/`1`.
- `A` Store plate carrier (move inside), `J` Present plate carrier (move outside).
- `S` Read plate: no arguments; uses the currently loaded assay definition.
- `d` Read well set: 33-byte payload (8 wells × row/col as ASCII "01"-"16"/"01"-"24", unused wells "00"), plus position byte `'0'`-`'3'`, terminated by `<ETX>`; returns ELx-format data only.
- `V` Set assay definition: 170-byte table. Wavelength fields are 3 ASCII digits; numeric interval/count/time fields are 16-bit little-endian integers (assumed, based on Appendix B constraints). Default/unused fields should be 0.
  - Host flow: send `V`, wait for `<ACK>`, then transmit 170-byte table and read status string response.

## Data response notes (high level)
- ELx format uses RS/ETX framing with checksum and final terminator (CTRL-Z).
- 312 format returns a fixed 8x12 plate matrix with assay name and extra chars.
- For reads, status string indicates errors; data is suppressed if error is set.
