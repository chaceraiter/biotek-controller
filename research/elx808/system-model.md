# BioTek ELx808 — System Model (Draft)

Scope: Build a mental model of how the ELx808 is put together (HW/SW/storage) and what we need to learn to control it and retrieve data via a modern host computer.

Status: Draft, based on a service manual excerpt provided by the user; may vary by hardware revision/year.

## High-level goal

Establish reliable communications with the instrument (likely RS-232), discover the command/protocol surface area, and build host-side software to:
- configure runs (assay/program parameters),
- start/stop runs safely,
- retrieve raw/processed results and metadata,
- view/export data for experiments.

## Architecture (as inferred)

### Compute core
- CPU: 16-bit Intel 80C186EB (U42), 16.0 MHz.
- Clock: derived from 32.0 MHz crystal (U40).
- Reset: solid-state reset device (U41).
- Real-time clock: on the display board (U4) with battery backup (BT1, 3.0 V lithium coin).

### Memory regions and what they likely contain

The excerpt describes several distinct non-volatile and volatile memory areas:

#### BIG FLASH EPROM (U33, U45; 16 × 524,288 bits)
- Purpose: storage for “application programs”; described as “instrument Basecode (Operating System)”.
- Notes:
  - Basecode can be loaded via RS-232.
  - Carrier alignment offset values (Auto-Calibration values) are stored here.

#### QUICK FLASH EPROM (U34, U46; 16 × 131,072 bits)
- Purpose: “variable assay parameter storage”; described as “instrument Assay Configuration Files”.
- Notes:
  - Defined “reader programs” that perform read functions.
  - User-modified; up to 55 definable programs.
  - Downloaded via “Extensions” software or “Download Utility”.
  - Excerpt claims these must be downloaded before the instrument operates properly.

#### STATIC RAM (U35, U47; 16 × 131,072 bits)
- Purpose: working memory for program operation (runtime state).

#### EPROM (U36, U48; 16 × 32,768 bits)
- Purpose: boot-up program (bootloader).

## Operational model (proposed)

### Boot and run lifecycle (hypothesis)
1. Bootloader (EPROM) starts and initializes CPU + essential peripherals.
2. Bootloader locates and starts Basecode from BIG FLASH.
3. Basecode loads/validates:
   - calibration offsets (BIG FLASH),
   - assay/program configurations (QUICK FLASH),
   - RTC/time settings (RTC).
4. Instrument UI allows selecting one of ~55 programs, executing read(s), and storing results in RAM and/or internal non-volatile storage.
5. Host communications (RS-232) allow:
   - system-level operations (identify/version/status, basecode update),
   - program/config download and management,
   - initiating reads / retrieving results.

### “Basecode” vs “Assay Configuration”
- Basecode: device OS/firmware; likely updated rarely, and may include a serial “download/upgrade” mode.
- Assay configuration: parameter sets (“programs”) defining run mode, wavelength/filter settings, timing, plate geometry, etc. These may be required for meaningful operation, depending on what’s already loaded.

## Interfaces we need to characterize

### RS-232 link
Unknowns we need to discover/confirm:
- Connector type (DB9/DB25), DTE/DCE orientation, and whether a null-modem is required.
- Serial settings: baud rate(s), data bits, parity, stop bits, flow control (RTS/CTS vs XON/XOFF).
- Session behavior: prompt-based? binary framed protocol? line-oriented ASCII? command/response?
- Upload/download mechanism: raw protocol vs XMODEM/YMODEM/ZMODEM vs bespoke.
- Any service/bootloader mode entry mechanism (key combo at power-on? jumper? special serial command?).

#### What we know so far (from user observation)
- The instrument has two visible external ports: one labeled “serial” and one labeled “parallel”.
- The “serial” port is a DB25 male connector (pins).
- The “parallel” port is a DB25 female connector (sockets).
- The user’s USB cable terminates in a DB25 female connector and mates with the instrument’s “serial” port.

#### Serial pinout (from service manual screenshot)
See `research/elx808/ports-and-pinouts.md`.

#### Serial settings (from operator manual excerpt)
- Default: 2400 baud, 8 data bits, 2 stop bits, no parity (2400 8N2).
- User-selectable baud rates: 1200, 2400, or 9600.
- Data bits/stop bits/parity are not user-configurable.

#### Computer-control behavior (from Appendix B excerpt)
- Computer-controlled kinetic assays can use up to three wavelengths.
- Under computer control, onboard blanking and data reduction are suppressed and raw data is returned (can include >3.000 OD).

#### RS-232 electrical layer (hint)
- The service manual reportedly mentions an “RS232 driver/receiver” IC. If accurate, that strongly suggests the instrument port uses true RS-232 voltage levels (not TTL UART), but it does not by itself reveal baud/parity/protocol. The exact part number/reference designator is worth confirming (it may be “IC1080” rather than “LT1080”).

### Software ecosystem mentioned
- “Extensions” software
- “Download Utility”

We should treat these as hints that:
- there is a defined download protocol and file format for programs,
- there may be a “PC side” utility that speaks an established command set.

## Risks / constraints
- Firmware update via RS-232 implies there are states where we could brick functionality if we send the wrong data. Early work should focus on read-only interrogation and passive observation.
- “Must be downloaded before the instrument will operate properly” could mean:
  - a new/blank unit requires program/config download to do anything beyond basic UI,
  - or certain workflows depend on configured programs even if the instrument “does something” out of the box.

## Open questions

Hardware / revision:
- What exact rear-panel ports exist on this unit, and which is intended for host control?
- Is there evidence the unit already has Basecode + programs loaded (e.g., it boots to a functional menu with selectable programs)?
- Any displayed firmware/basecode version on startup/menus?

Protocol:
- Is the control protocol documented in the service manual or a separate “communications” manual?
- Does the device support a “printer” output mode distinct from “computer control”?
- What are the message framing and checksum rules (if any)?

File formats:
- What is the structure of “Assay Configuration Files”?
- How are results encoded (ASCII tables vs binary blocks), and what metadata is included?

Calibration:
- Auto-Calibration stores offsets in BIG FLASH; does host control require handling or verifying calibration state?

## Source excerpt (verbatim)

The ELx808 uses a 16 bit 80C186EB (U42)
microprocessor which runs at 16.0 MHZ. The clock frequency is derived from a 32.0 MHZ crystal (U40).
The power on reset is provided via a solid-state device (U41). The system has a real time clock (U4 on
the display board) that has an external battery (BT1 3.0 volt lithium coin on the display board).

Memory
The CPU uses a variety of memory. A block of BIG FLASH EPROM (U33,U45 16X524288 bits)
is used as storage for application programs. A smaller block of QUICK FLASH EPROM (U34,U46
16X131072 bits) is used for variable assay parameter storage. A block of STATIC RAM (U35,U47
16X131072 bits) is used for program operation storage and a block of EPROM (U36,U48 16X32768 bits)
is used to store the boot up program.

The Big Flash requires the instrument Basecode (Operating System) loaded via the RS232 port.
This software is the reader’s operating system.

The Quick Flash requires the instrument Assay Configuration Files loaded via the RS232 port.
This software is the reader programs that are defined to perform the read functions. This is user modified
to created individual read programs. There are fifty-five (55) definable programs. The download of these
files are performed using the Extensions software or the Download Utility.
These programs must be downloaded before the instrument will operate properly.

The carrier alignment offset values (Auto-Calibration values) are stored in the BIG FLASH.
These alignment offsets are determined by executing the Auto-Calibration program that is included in the
ELx808 basecode. An alignment plate (BTI part # 73302508) is required to find the offsets.
