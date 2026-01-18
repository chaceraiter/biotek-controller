<!-- SYSTEM FILE - AI chat summary for project continuity. -->

# 2026-01-17 — Web UI + Validation Wrap‑Up

## Summary
- Implemented short‑run validation flow (ECO60/ECO30 profiles) with incremental CSV output and automated interval checks.
- Added playback decode for read‑wells logs and manifest output for runs.
- Fixed multiple CLI edge cases for global flags after subcommands and streaming buffer handling.
- Built and shipped a small local web UI to run ECO60 validation or ECO590 reads with live log streaming.
- Ran ECO60 validation on hardware; captured two intervals and produced CSV/manifest/log files.

## Decisions
- Keep ECO590 as the standard 48‑hour protocol; use ECO60 for validation.
- Treat missing final terminator as a warning by default; allow strict enforcement via `--strict-complete`.
- Provide a minimal local web UI rather than a large framework.

## Code changes
- `tools/elx808/assay_profiles.json`
  - Added `ECO60` and `ECO30` short‑run profiles.
- `tools/elx808/control_stack.py`
  - Added `run-ecoplate` wrapper with incremental CSV logging.
  - Added `validate-short-run` with restore, interval validation, and relaxed terminator check by default.
  - Added ECO60 default `quiet=240` and `timeout=900`.
  - Added `--manifest` output (JSON run summary).
  - Allowed global flags after subcommands (`--confirm-run`, `--quiet`, `--timeout`, `--log`, `--manifest`).
  - Fixed streaming buffer mutation (ensure `bytearray`).
- `tools/elx808/playback_decode.py`
  - Added `--mode read-wells` and optional `--well` labels for playback CSV.
- `tools/elx808/web_ui.py`
  - New local web UI server with live log streaming and run controls.
- `tools/elx808/README.md`
  - Documented validation, playback decode, manifest output, and web UI usage.

## Hardware runs & outputs
- 8‑well capture:
  - `/tmp/elx808-read-wells.log`
  - `/tmp/elx808-read-wells.csv`
- ECO60 validation (successful, 2 intervals):
  - `/tmp/elx808-validate.csv`
  - `/tmp/elx808-validate.log`
  - `/tmp/elx808-validate.json`

## Issues encountered
- Missing final CTRL‑Z terminator in read responses; handled as warning unless `--strict-complete` is set.
- CLI rejected global flags after subcommands; fixed in `control_stack.py`.
- Streaming read buffer became immutable; fixed by converting trailing bytes back to `bytearray`.

## Next steps
- Start new chat and use `for-humans/paste-this-into-new-ai-chats.txt`.
- Use the web UI at `http://127.0.0.1:8088` for validation runs.
- Validate ECO590 long‑run behavior before live experiments.
