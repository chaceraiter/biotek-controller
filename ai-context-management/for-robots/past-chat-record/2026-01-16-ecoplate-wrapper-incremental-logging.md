<!-- SYSTEM FILE - AI chat summary for project continuity. -->

# 2026-01-16 — EcoPlate Wrapper + Incremental CSV Logging

## Summary
- Discussed keeping the standard 48-hour ECO590 protocol unchanged while enabling faster development workflows.
- Implemented a simple wrapper command to run the standard ECO590 profile and produce CSV output.
- Added incremental CSV logging so plate data is written as each interval arrives (no need to wait for completion).
- Confirmed expected runtime for ECO590 (48 hours) and added auto-expanded timeouts for long runs.
- Committed and pushed changes to `origin/main` (commit `1fb8c03`).

## User decisions
- Keep ECO590 protocol as the standard 48-hour run (15-minute interval × 192 reads).
- Add incremental output instead of waiting for a full run to finish.
- Create a wrapper for the standard ECO590 protocol (and leave ECO60 optional/for later).

## Code changes
- `tools/elx808/control_stack.py`
  - Added `run-ecoplate` subcommand that loads an assay profile (default ECO590) and then runs `read-plate`.
  - Added `--confirm-run` as a shortcut to set all confirm flags.
  - Auto-adjusted `--timeout` and `--quiet` based on assay profile unless explicitly provided.
  - Added `--incremental` option to `read-plate`.
  - Implemented incremental CSV logging:
    - `_IncrementalPlateCsvWriter` writes header once and appends rows per interval.
    - `_read_plate_streaming` parses ELx blocks as they stream in and writes rows per block.
    - `run-ecoplate` defaults to incremental CSV output.
  - Added helper utilities to load assay settings from a profile for internal use.
- `tools/elx808/README.md`
  - Documented `run-ecoplate` usage and incremental CSV logging example.

## Commands added/updated
- `run-ecoplate`:
  - `python3 tools/elx808/control_stack.py --port /dev/cu.usbserial-XXXX run-ecoplate --confirm-run --csv /tmp/elx808-ecoplate.csv`
  - Uses incremental logging by default and expands `--timeout`/`--quiet` automatically.
- `read-plate --incremental`:
  - `python3 tools/elx808/control_stack.py --port /dev/cu.usbserial-XXXX read-plate --confirm-write --confirm-movement --confirm-read --decode --csv /tmp/elx808-read-plate.csv --incremental`

## Notes on behavior
- ECO590 run time is ~48 hours (192 reads × 15 minutes).
- Incremental logging writes CSV rows per interval and prints interval progress to stdout.
- Final ELx response handling is preserved and logged after streaming.

## Outstanding items / next steps
- Decide whether to add a short-run ECO60 profile for quick validation runs.
- Consider a playback/decode mode for existing logs to iterate on parsing without hardware time.
