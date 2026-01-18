<!-- SYSTEM FILE - AI chat summary for project continuity. -->

# 2026-01-18 — Instrument Errors + Post‑Read Status

## Summary
- Reviewed CSV/log output from the latest run; only the first interval completed (590 + 750), and the read aborted after the first interval (DLE).
- Mapped error codes 2331/2332 to `LAMP ERR` with test type 1 (5V) vs 2 (24V).
- Added UI-facing error decoding and recommendations based on Appendix B status codes.
- Added a post-read `o` status query to capture error codes automatically in run logs.

## Decisions
- Always issue `o` after read commands so errors are captured in logs even when the read ends early.
- Surface a human-readable alert panel in the UI with suggested recovery steps for each error category.

## Code changes
- `tools/elx808/web_ui.py`
  - Decode ELx/312 status codes with descriptions.
  - Add alert panel with recommendations for error recovery.
  - Treat attention/disconnected as non-startable states.
- `tools/elx808/control_stack.py`
  - Issue post-read `o` status after `read-plate` and `read-wells`.
- `ai-context-management/for-robots/current-work/current-context-for-new-chat.md`
  - Updated recent changes for error decoding + post-read status logging.

## Hardware runs & outputs
- `/private/tmp/elx808-20260118-152813.log`
  - Read returned two wavelength blocks for interval 1, then aborted (DLE).
- `/Users/r8r/Downloads/elx808-20260118-152813.csv`
  - 192 rows = 96 wells × 2 wavelengths for interval 1 only.

## Next steps
- Run another short test and confirm `read-plate-status` lines appear in the log.
- If 23xx errors persist, run self-test and power-cycle per Appendix B guidance.
