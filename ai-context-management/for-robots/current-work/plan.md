# Project Plan

## Planned (not implemented yet)
- Add a "Reconnect" button in the web UI to reattach the interface to the device without interrupting an in-progress assay; reconnect should be status-only by default.
- Add reconnect-associated actions for retrieving test data and updating test protocols, gated behind explicit confirmations and safe-command checks.
- Document the required protocol support for reconnect/data retrieval (commands, data retention behavior) before enabling these actions.
- Implement persistent storage on the Mac for instrument test/experiment data (for example ECO590 runs) and expose it via the web UI; requires confirmed instrument data-retrieval commands if the data only lives on the device.
- Add a real database (Postgres or MySQL on macOS) to store, display, and retrieve all run results; store every cell for every test and wavelength.
- Start storing new runs only; seed dummy data for UI/testing.
- Web UI goals: per-run views now; future in-browser plots; cross-test search with joins (for example: soils with pH > 8 and substrate depletion in well A8 within 24 hours).
- Data retention: keep all runs by default; allow deletes for test/failed runs.

## Clarifications needed
- Choose database engine (Postgres vs MySQL) and target location on the Mac (data dir, credentials/port).

## Constraints
- Keep read-only and state-changing actions clearly separated; use confirmation flags for any state change.
- Do not implement protocol/assay download flows until the spec and rollback plan are verified.
