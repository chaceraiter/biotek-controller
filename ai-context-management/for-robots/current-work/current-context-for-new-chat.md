<!-- TEMPLATE FILE - Fill this out and update it regularly with the current state of your project. -->

# Current Context for New Chat

## Current state
- We have an initial system model from a service manual excerpt describing CPU (80C186EB) and memory regions (BIG FLASH basecode, QUICK FLASH assay configs, RAM, boot EPROM).
- The instrument has two visible DB25 ports: a DB25 male port labeled “serial” and a DB25 female port labeled “parallel”.
- Service manual pinout captured for both ports; serial uses pins 1/7 GND, 2 TX, 3 RX, 4 RTS, 5 CTS, 6 DSR, 8 DCD, 20 DTR.
- Operator manual excerpt indicates default serial settings: 2400 baud, 8 data bits, 2 stop bits, no parity (2400 8N2), with baud selectable to 1200 or 9600.
- Appendix B excerpt indicates that under computer control the instrument suppresses onboard blanking/data reduction and returns raw data (including values > 3.000 OD); supports kinetic assays using up to three wavelengths.
- KCjunior setup page recommends host serial settings of 9600 8N2 and references an “EOT Character” setting (default value not yet captured).
- User reports the instrument baud rate is currently set to 9600 and the host target is macOS/Unix using a USB→USB‑C adapter as needed.

## What’s working
- Documentation scaffolding exists under `research/elx808/` capturing the system model, pinouts, and a safe serial bring-up plan.

## Unknowns / active questions
- Serial parameters (baud/parity/stop bits, flow control).
- Appendix B “computer control protocol” details (command set / framing / required protocol).
- Whether the host cable/adapter is DTE vs DCE (whether a null-modem/cross-over is required).
- Whether the ELx808 emits any banner/status on serial at boot and what command set/protocol is supported.

## Next steps
- Confirm cabling behavior (straight vs null-modem) and identify USB-serial adapter details on the host.
- Find RS-232 settings and any remote-control/download protocol references in the service manual.
- Capture first serial transcripts (boot output + minimal “poke” attempts) for protocol inference.
