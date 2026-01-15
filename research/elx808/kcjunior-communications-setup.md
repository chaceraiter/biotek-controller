# BioTek ELx808 — KCjunior Communications Setup (Manual Page Notes)

Source: user-provided screenshot titled “Controlling the Reader With KCjunior”.

## What this page tells us
- The recommended KCjunior serial configuration for ELx808 communication is:
  - Baud rate: **9600** (with note: change baud rate on the reader if necessary)
  - Data bits: **8**
  - Parity: **None**
  - Stop bits: **2**
  - “EOT Character”: **keep the default number** (value not shown in screenshot)
- The page references using serial cable part number **PN 75053** between PC and reader.
- KCjunior includes a “Test Communications” action, implying a deterministic link-level probe we can mimic once we see the underlying command(s).

## Reader model options shown in KCjunior
- `ELx808`, `EL808`
- `ELx808I`, `EL808I`
- `ELx808U`, `EL808U`
- `ELx808UI`, `EL808UI`

## Open question
- What exact numeric value does KCjunior use as its default “EOT Character”?
  - If we can’t recover it from KCjunior UI/docs, we can infer it from Appendix B protocol framing or by observing traffic from a working KCjunior session.
  - Until then, we can proceed with serial bring-up and focus on Appendix B’s on-wire message format; the EOT value only matters once we know whether the protocol uses it as a terminator/framing byte.
