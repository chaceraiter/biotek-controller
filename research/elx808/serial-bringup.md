# BioTek ELx808 — Serial Bring-up Plan (Safe / Read-only First)

Goal: Establish a reliable RS-232 link and determine whether we need a null-modem/cross-over, which serial settings are correct, and what (if anything) the instrument emits/responds with.

## Safety rules (early stage)
- Do not attempt any firmware/basecode or assay download flows yet.
- Prefer passive listening and read-only queries until we can positively identify commands and their effects.

## Known physical facts
- Instrument “serial” port is DB25 male; pinout in `research/elx808/ports-and-pinouts.md`.
- Instrument also has a separate DB25 “parallel” port (ignore for RS-232 work).

## Step 1: Identify the host serial device
On the host PC, identify what device node the USB adapter exposes (e.g., `/dev/ttyUSB0`, `/dev/tty.usbserial-*`, etc.) and confirm you can open it.

Record:
- OS (macOS/Linux/Windows),
- adapter chipset/model if available,
- device path.

## Step 2: Determine whether cross-over is required
Because the ELx808 pinout matches DB25 DTE (TX on 2, RX on 3), the host side must effectively be DCE, or you must insert a null-modem/cross-over.

Practical approach:
1. Try “straight” as-is (no extra adapter).
2. If there is no response at all after we confirm settings, try inserting a DB25 null-modem/cross-over (swaps at least pins 2 and 3; often also swaps handshake lines).

## Step 3: Probe serial settings (listen first)
Start by *only listening* while power-cycling the instrument:
- Open the port with candidate settings.
- Power-cycle the ELx808.
- Watch for any banner, status line, or binary burst.

Operator-manual-derived settings to try first (highest confidence):
- 2400 8N2, no parity (default)
- 1200 8N2, no parity (optional)
- 9600 8N2, no parity (optional)

If testing with KCjunior-derived assumptions, prioritize 9600 8N2.

If the manual specifies settings, use those instead of probing.

## Step 4: Gentle “poke” (minimal writes)
If passive listening yields nothing, try sending:
- `CR` (0x0D)
- `LF` (0x0A)
- `CRLF`
- `?` + `CR`

Then listen for a response. If responses are garbled, baud/parity is wrong.

## Step 5: Capture evidence for protocol analysis
For every attempt, capture:
- exact serial settings used,
- whether cross-over was used,
- raw bytes received (hex dump if binary),
- timestamps (even approximate).

This log becomes the basis for inferring framing, prompts, and command/response behavior.
