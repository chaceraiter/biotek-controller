<!-- SYSTEM FILE - AI chat summary for project continuity. -->

# 2026-01-16 — Short-Run Validation Plan

## Summary
- Built a short-run validation workflow to prove multi-interval capture without waiting 48 hours.
- Added ECO60/ECO30 assay profiles for quick kinetic verification.
- Added a `validate-short-run` command that sets the short assay, runs a plate read with incremental CSV logging, validates interval count/completeness, and restores ECO590 by default.
- Implemented a playback decoder script to convert captured logs into CSV without hardware.
- Ran a short 8-well capture on the real instrument and wrote `/tmp/elx808-read-wells.log` + `/tmp/elx808-read-wells.csv`.
- Fixed validation CLI edge cases (`--confirm-run`, `--quiet`, `--timeout`, `--log`) when passed after subcommands.
- Fixed streaming read bug in `_read_plate_streaming` where the buffer could become immutable.
- Completed an ECO60 validation run: both intervals captured; missing terminator treated as warning.
- Added ECO60 default quiet/timeout for validation and added JSON run manifests.
- Playback decoder now supports read-wells logs with optional well labels.

## Decisions
- Validation should focus on a short ECO60 run first and restore ECO590 afterward.
- Playback mode is the fastest iteration loop for parsing/reporting work.
- Relax the “missing terminator” check by default; strict mode available via `--strict-complete`.

## Code changes
- `tools/elx808/assay_profiles.json`
  - Added `ECO60` and `ECO30` short-run profiles (dual wavelength, 60s/30s interval, 2 reads).
- `tools/elx808/control_stack.py`
  - Added `validate-short-run` subcommand with optional restore, auto timeout/quiet sizing.
  - Added interval/count validation logic to flag incomplete runs.
  - Allowed global flags after subcommands (`--confirm-run`, `--quiet`, `--timeout`, `--log`).
  - Fixed `_read_plate_streaming` buffer mutation (ensure `bytearray`).
  - Added `--strict-complete` to enforce terminator if desired.
  - Added ECO60 default `quiet=240` and `timeout=900` for validation runs.
  - Added `--manifest` output with run metadata and summaries.
- `tools/elx808/playback_decode.py`
  - New script to decode control-stack or serial-capture logs into CSV without hardware.
  - Added `--mode read-wells` and `--well` labels for read-wells playback.
- `tools/elx808/README.md`
  - Documented `validate-short-run` usage and playback decoder.
  - Documented manifest output and read-wells playback example.

## Commands used
- 8-well capture on hardware:
  - `python3 tools/elx808/control_stack.py --port /dev/cu.usbserial-ABSCDEPH --log /tmp/elx808-read-wells.log read-wells --well A1 --well A2 --well A3 --well A4 --well B1 --well B2 --well B3 --well B4 --confirm-write --confirm-movement --confirm-read --decode --csv /tmp/elx808-read-wells.csv`
- ECO60 validation run with longer quiet/timeout:
  - `python3 tools/elx808/control_stack.py --port /dev/cu.usbserial-ABSCDEPH validate-short-run --confirm-run --csv /tmp/elx808-validate.csv --quiet 240 --timeout 900 --log /tmp/elx808-validate.log`
- ECO60 validation run with defaults + manifest:
  - `python3 tools/elx808/control_stack.py --port /dev/cu.usbserial-ABSCDEPH validate-short-run --confirm-run --csv /tmp/elx808-validate.csv --manifest /tmp/elx808-validate.json --log /tmp/elx808-validate.log`

## Current state / next steps
- ECO60 validation captured both intervals; missing terminator handled as warning by default.
- Manifest output verified at `/tmp/elx808-validate.json`.
- If needed, tune `--quiet`/`--timeout` defaults or set `--strict-complete` for more conservative checks.
