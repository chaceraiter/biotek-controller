# BioTek ELx808 — Configuration / Comms Discovery Checklist

Goal: Collect the minimum hard facts needed to start safe serial probing and eventually implement host-side control + data retrieval.

## 1) Physical interface inventory
- Rear panel photos (straight-on, readable labels).
- Connector type(s): DB9/DB25, RJ-style, mini-DIN, etc.
- Port labeling: “RS-232”, “Computer”, “Printer”, “Serial”, “Aux”, “Service”.
- Confirm whether the port is isolated/differential or plain RS-232 (rare, but worth noting).
Known so far:
- Instrument has a DB25 male “serial” port and a DB25 female “parallel” port.

## 2) Cabling assumptions to validate
- DTE vs DCE behavior (does it act like a modem or a PC?).
- Null-modem required? (cross TX/RX) vs straight-through.
- Handshake requirements: RTS/CTS needed vs can run without hardware flow control.
- Grounding/shielding guidance from docs.
Hints from pinout:
- Serial port pin assignment matches DB25 DTE (TX on 2, RX on 3), so a host that is also DTE will need a null-modem/cross-over.

## 3) Serial settings to discover
Try to find in manuals first; otherwise probe empirically.
- Baud rates to test first: 2400 (default), then 1200 or 9600 (user-selectable per operator manual).
- Data framing to test first: 8N2 (per operator manual), then only broaden if evidence suggests otherwise.
- Flow control to test: none, RTS/CTS, XON/XOFF.

## 4) “Safe” first interactions (read-only)
We want the smallest set of actions that won’t change instrument state.
- Does the instrument print any banner/version on connect?
- Does it respond to any “help”/“?”/CR/LF behavior?
- Any status/ID query?
- Any command to dump configuration/program list without modifying it?
- Any mention of an “EOT character” or required terminator in the protocol docs (Appendix B)?

## 5) Identify firmware/config state
From UI and/or serial responses:
- Basecode / firmware version.
- Whether assay programs exist; how many; names/IDs.
- Whether it indicates “missing programs” or similar errors.
- Whether it has a “PC control” mode toggle.

## 6) Download/update pathways (high risk)
These come later, after we can reliably identify/monitor state.
- How to enter download mode (UI/menu? boot key combo? jumper?).
- Whether it uses XMODEM/YMODEM/ZMODEM or a custom framing.
- What files are expected for:
  - Basecode (BIG FLASH),
  - Assay configuration (QUICK FLASH).
- Any checksum/signature/version gating.

## 7) Data retrieval
- Where results live (volatile vs persisted).
- Commands to retrieve:
  - last run,
  - a given program/run ID,
  - raw absorbance matrix vs processed values.
- Output encoding: ASCII tables, CSV-like, or binary blocks.
- Units/metadata: wavelength, gain, plate format, timestamp.

## 8) What to capture next from your docs
If you have these pages/sections, they answer most unknowns quickly:
- RS-232 pinout and required cable type.
- Serial settings (baud/parity/flow).
- Appendix B: computer-control protocol details.
- Any mention of an “EOT character” (what value it is, and whether it is sent as a terminator or used for framing).
- Command set / remote control protocol.
- “Download Utility” / “Extensions” behavior and screenshots.
- Error codes relating to missing programs/calibration.
- Any schematic/BOM notes naming the RS-232 driver/receiver IC (part number + reference designator).
