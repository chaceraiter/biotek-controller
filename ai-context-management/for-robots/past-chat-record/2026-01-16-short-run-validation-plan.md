<!-- SYSTEM FILE - AI chat summary for project continuity. -->

# 2026-01-16 — Short-Run Validation Plan

## Summary
- Built a short-run validation workflow to prove multi-interval capture without waiting 48 hours.
- Added ECO60/ECO30 assay profiles for quick kinetic verification.
- Added a `validate-short-run` command that sets the short assay, runs a plate read with incremental CSV logging, validates interval count/completeness, and restores ECO590 by default.
- Implemented a playback decoder script to convert captured logs into CSV without hardware.
- Ran a short 8-well capture on the real instrument and wrote `/tmp/elx808-read-wells.log` + `/tmp/elx808-read-wells.csv`.

## Decisions
- Validation should focus on a short ECO60 run first and restore ECO590 afterward.
- Playback mode is the fastest iteration loop for parsing/reporting work.

## Code changes
- `tools/elx808/assay_profiles.json`
  - Added `ECO60` and `ECO30` short-run profiles (dual wavelength, 60s/30s interval, 2 reads).
- `tools/elx808/control_stack.py`
  - Added `validate-short-run` subcommand with optional restore, auto timeout/quiet sizing.
  - Added interval/count validation logic to flag incomplete runs.
- `tools/elx808/playback_decode.py`
  - New script to decode control-stack or serial-capture logs into CSV without hardware.
- `tools/elx808/README.md`
  - Documented `validate-short-run` usage and playback decoder.

## Commands used
- 8-well capture on hardware:
  - `python3 tools/elx808/control_stack.py --port /dev/cu.usbserial-ABSCDEPH --log /tmp/elx808-read-wells.log read-wells --well A1 --well A2 --well A3 --well A4 --well B1 --well B2 --well B3 --well B4 --confirm-write --confirm-movement --confirm-read --decode --csv /tmp/elx808-read-wells.csv`

## Current state / next steps
- Run `validate-short-run` to confirm 2 intervals are captured and CSV grows incrementally.
- If validation passes, proceed toward UI work for “real-life” runs; if not, tune timeouts/quiet or framing logic.
