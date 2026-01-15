<!-- TEMPLATE FILE - Fill this out with your project's architecture and technical decisions. -->

# Project Architecture

This architecture is expected to evolve as we learn the ELx808’s protocol.

## System Overview
- **Instrument layer:** BioTek ELx808 microplate reader with RS-232 “serial” port and a separate “parallel” port.
- **Host connectivity:** USB-to-RS232 adapter/cable to a modern computer.
- **Protocol discovery tooling:** scripts/utilities to probe serial settings, capture raw traffic, and replay minimal queries.
- **Core protocol library:** parsing/encoding of messages, framing, checksums, and command/response semantics.
- **Applications:**
  - diagnostic CLI (connect, identify, status, dump config, dump results),
  - later: experiment/run orchestration and data export,
  - later: UI for viewing runs and metadata.

## Technology Stack
- **Undecided.** Likely start with Python for rapid serial/protocol research; revisit language choice once the protocol is understood and stable.
- Data storage/export targets: CSV/JSON initially; optional SQLite later for run history.

## Key Design Patterns
- **Layered separation:** transport (serial), protocol framing, domain commands, app workflows.
- **Append-only logs:** keep raw I/O logs for reproducibility and debugging across sessions.
- **Capability detection:** query instrument ID/version and adapt to known protocol variants.

## Technical Decisions
- Prioritize safety: avoid firmware/update paths until the protocol is understood.
- Prefer read-only interrogation first; introduce state-changing commands only with explicit confirmation of behavior.
