# BioTek ELx808 — Ports and Pinouts (From Service Manual)

Source: screenshot provided by user from `Biotek_ELx808_-_Service_manual.pdf` (frankshospitalworkshop.com).

## Serial port (DB25)

Pin | Signal
---:|:------
1 | GND
2 | TX
3 | RX
4 | RTS
5 | CTS
6 | DSR
7 | GND
8 | DCD
9–18 | NC
19 | NC
20 | DTR
21–25 | NC

Implications:
- Pin assignment matches the RS-232 DB25 *DTE* convention (TX on 2, RX on 3, SG on 7).
- If the host adapter is also DTE (common for many USB-to-serial dongles), a null-modem (cross-over) is required.
- If the host adapter presents as DCE, a straight-through connection is correct.

## Parallel port (DB25)

Pin | Signal
---:|:------
1 | PSTROBE
2 | D0
3 | D1
4 | D2
5 | D3
6 | D4
7 | D5
8 | D6
9 | D7
10 | NC
11 | BUSY
12 | NC
13 | ON-LINE
14 | NC
15 | NC
16 | RESET
17 | NC
18 | GND
19 | GND
20 | GND
21 | GND
22 | GND
23 | GND
24 | GND
25 | GND

## Cable part numbers (as shown)
- BioTek `#75053` is a DB9F to DB25F serial cable.
- BioTek `#75049` is a DB25M to Centronix parallel cable.

