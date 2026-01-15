<!-- TEMPLATE FILE - Fill this out with your project's vision and goals. -->

# Project Vision and Goals

## Vision

Build a modern, reproducible way to control and extract data from a BioTek ELx808 microplate reader (older unit, likely ~1995–2002 era) without relying on the original vendor “instrument PC” + proprietary Windows software.

## Why

- The instrument has internal firmware, but the original peripheral PC/software is missing.
- To use the reader for experiments, we need host-side I/O: configuring runs, starting/stopping, and pulling results.
- The project is research- and testing-heavy: the first milestone is understanding and documenting how the device communicates.

## Who it’s for

- The project owner and other tinkerers/researchers with legacy ELx808 units.
- Labs/hackers who want to integrate the reader into modern workflows (scripts, notebooks, pipelines).

## Near-term goals (milestones)

- Establish reliable RS-232 communication with the instrument.
- Identify protocol surface area (commands, responses, framing/checksums, flow control).
- Retrieve run data in a deterministic, parseable form.
- Capture a “protocol spec” and a repeatable set of tests/logs.

## Long-term goals

- Create control + data viewing/export software (initially minimal CLI tooling, later potentially a UI).
- Support multiple ELx808 revisions if differences exist (detectable via ID/version).
