<!-- TEMPLATE FILE - Fill this out with your project's code patterns and conventions. -->

# Code Patterns and Conventions

## General
- Prefer small, testable modules over monolith scripts.
- Keep reverse-engineering artifacts (logs, notes, extracted tables) under a dedicated `research/` area.

## Logging and reproducibility
- Treat serial transcripts as first-class artifacts (timestamped, settings recorded, raw bytes preserved).
- When documenting protocol behavior, always include:
  - serial settings (baud/parity/flow),
  - wiring/cross-over assumptions,
  - exact bytes on the wire (hex when binary).

## Safety conventions
- Separate **read-only** commands from **state-changing** commands in the API and CLI.
- Do not implement or run basecode/assay download flows until we have a verified spec and rollback plan.

## Testing (initial)
- Prefer deterministic parser/encoder tests once message framing is known.
- For hardware-in-the-loop tests, keep them opt-in and clearly labeled.
