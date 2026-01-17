<!-- TEMPLATE FILE - Fill this out and update it regularly with the current state of your project. -->

# Current Context for New Chat

## Current state
- We have an initial system model from a service manual excerpt describing CPU (80C186EB) and memory regions (BIG FLASH basecode, QUICK FLASH assay configs, RAM, boot EPROM).
- The instrument has two visible DB25 ports: a DB25 male port labeled “serial” and a DB25 female port labeled “parallel”.
- Service manual pinout captured for both ports; serial uses pins 1/7 GND, 2 TX, 3 RX, 4 RTS, 5 CTS, 6 DSR, 8 DCD, 20 DTR.
- Operator manual (Appendix B) confirms fixed framing: 8 data bits, no parity, 2 stop bits; baud selectable 1200/2400/9600; RS-232 port is DTE (TX pin 2, RX pin 3).
- Appendix B command set captured in `research/elx808/computer-control-notes.md` (ACK/NAK, RS/ETX framing, status formats, core commands including `*` self-test and `o` status).
- KCjunior setup recommends host 9600 8N2 and keeping the EOT character at default.
- Host is macOS/Unix; USB-serial adapter enumerates as `/dev/cu.usbserial-ABSCDEPH` (FT232R USB UART).
- Protocol probe results: `o` returns ELx status `0000` (no error), `e` returns part `7340201  Version 3.15` with 312 status `000`.
- Using the control stack, `n1` (set status to ELx) causes subsequent `o` and `e` responses to return ELx status `0000`.
- `get-wavelengths` (`W`) returns installed filters: 405, 450, 490, 590, 650, 750.
- EcoPlate assay loaded as dual-wavelength subtraction (590/750) with 15-minute interval, 192 reads; status returns `ELx:0000`.
- `T` is acknowledged but does not trigger self-test; `*` self-test runs successfully without error.

## Recent changes
- Added `tools/elx808/protocol_probe.py` (safe status/version probe + status parsing + `--set-status`).
- Added `tools/elx808/adapter_probe.py` and fixed `tools/elx808/serial_capture.py` macOS speed handling.
- Added `tools/elx808/control_stack.py` read scaffolding (`read-plate`, `read-wells`) with ELx framing helpers and explicit `--confirm-read` gating.
- Added `set-assay` encoder for `V` (assay definition) with `--confirm-assay` safety gate and dry-run output.
- Added `tools/elx808/assay_profiles.json` and `set-assay --profile` support for reusable assay presets.
- Added `read-wells --decode` support to parse numeric values and optional CSV output.
- Added `read-plate --decode` support to export full-plate CSV (rows/cols configurable).
- Added `run-ecoplate` wrapper to apply ECO590 and run `read-plate`, with auto timeout/quiet sizing.
- Added incremental CSV logging for plate reads (`read-plate --incremental`), and enabled it by default for `run-ecoplate`.
- Added short-run assay profiles `ECO60` and `ECO30` for quick kinetic validation.
- Added `validate-short-run` to set a short assay, run `read-plate`, validate interval count/completeness, and restore ECO590.
- Added `playback_decode.py` to decode captured logs into CSV without hardware.
- Added playback decode for read-wells logs plus optional `--well` labels.
- Added `--manifest` to emit a JSON run summary (command, profile, timing, CSV/log paths, interval summary).
- Updated `validate-short-run` defaults for ECO60 (`quiet=240`, `timeout=900`) and relaxed terminator check by default.
- Added `get-wavelengths` command to query installed filters.
- Documented Appendix B protocol details and successful self-test in `research/elx808/*`.
- Converted EcoPlate and Gen5 PDFs into markdown + summaries under `docs/`.

## What’s working
- Documentation scaffolding exists under `research/elx808/` capturing the system model, pinouts, and Appendix B protocol details.
- `protocol_probe.py` can read status and basecode version; status normalization works (ELx vs 312).
- `*` self-test command runs and completes without error on the instrument.
- `set-assay` succeeds (ACK for `V` then status `0000`); ECO30/ECO60 quick assays used to validate kinetic reads.
- `read-wells` returns decoded numeric values; ECO30 test returned two intervals (`blocks=2 complete=True`).
- `read-plate` decoding writes CSV to `/tmp/elx808-read-plate.csv` (initial ECO60 run captured only first interval; needs longer timeout to capture second).
- `run-ecoplate` can run the standard ECO590 protocol and log CSV incrementally as intervals arrive.
- Short 8-well capture produced `/tmp/elx808-read-wells.log` and `/tmp/elx808-read-wells.csv`.
- ECO60 validation captured two intervals with default ECO60 quiet/timeout; missing terminator treated as warning by default.
- Manifest output verified at `/tmp/elx808-validate.json`.

## Unknowns / active questions
- Status format persistence (ELx vs 312) and when the reader auto-switches formats.
- Exact command/argument framing for read operations (`S`, `d`) and how errors propagate mid-stream.
- Best timeout/quiet settings for long kinetic runs beyond ECO60 (ECO590 still untested).
- Confirm whether the USB-serial adapter is true RS-232 level (FT232R often indicates TTL without level shifting).
- Gen5 COMPLETE user guide OCR: current PDF text extraction fails due to damaged PDF.

## Next steps
- Use `protocol_probe.py` to standardize status format (`n`) and test additional safe commands (`o`, `e`, `q`, `n`).
- Implement a minimal protocol wrapper for command/response parsing and status handling.
- Validate ECO590 long run behavior (timeouts, completeness) after UI scaffolding is in place.
- Decide on UI workflow: profile selection, run progress, CSV/manifest display, and error handling.
- Resolve Gen5 COMPLETE OCR (alternate PDF source or different OCR pipeline).
