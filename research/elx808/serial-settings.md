# BioTek ELx808 — Serial Communications Settings (Operator Manual Excerpt)

Source: user-provided excerpt from *ELx808 Operator’s Manual* section “Setting Communications Parameters”.

## Default communications parameters
- Baud rate: **2400**
- Data bits: **8**
- Stop bits: **2**
- Parity: **None**

Shorthand: **2400 8N2**

## User-configurable vs fixed
- User can change **baud rate** from 2400 to **1200** or **9600**.
- Data bits, stop bits, and parity are **not user-configurable** (always 8 data bits, 2 stop bits, no parity).

## KCjunior settings (from manual page screenshot)
- KCjunior recommends configuring the host for **9600 8N2** and changing the reader baud rate if needed.
- KCjunior has an “EOT Character” setting and instructs to keep its default value (exact value not shown).
- See `research/elx808/kcjunior-communications-setup.md`.

## Control/protocol references
- Manual states: “Appendix B contains information on required protocols for computer control of the reader.”
- Mentions compatibility with Bio-Tek KC4/KCjunior software and “standard communications software and/or RS232 protocols”.
- Mentions downloading Assay Definition Files created with “Extensions Define Reader Protocol” software over RS-232.
