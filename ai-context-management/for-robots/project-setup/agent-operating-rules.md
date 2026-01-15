<!-- TEMPLATE FILE - Fill this out with your project-specific operating rules for AI agents. -->

# Agent Operating Rules

This project is research-driven and involves controlling real lab hardware. Optimize for safety, traceability, and reproducibility.

## General Principles
- Be explicit about assumptions (especially around cabling, serial settings, and instrument state).
- Ask before proposing or performing any action that could change instrument firmware/configuration.
- Prefer plans/checklists and incremental experiments over large speculative implementations.

## Code Quality Standards
- Keep “protocol knowledge” documented in `research/` alongside sources and raw logs.
- Add tests once message formats are known; avoid overengineering before discovery is complete.

## Workflow Guidelines
- Update `research/` notes when new facts are learned (pinouts, settings, commands, quirks).
- Keep the AI context system (`ai-context-management/for-robots/current-work/*`) current when focus changes.

## Red Lines (Never Do This)
- Never attempt firmware/basecode flashing or “download utility” flows without explicit user approval and a verified procedure.
- Never recommend connecting TTL-serial directly to RS-232 pins (voltage-level mismatch risk).
