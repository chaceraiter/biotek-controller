<!-- TEMPLATE FILE - Fill this out with your project's current work focus. Update whenever focus shifts. -->

# Current Work Focus

This is a new project to regain host control of a legacy BioTek ELx808 microplate reader without the original vendor PC/software. The work is currently focused on building an accurate model of the instrument’s firmware/configuration storage and establishing reliable RS-232 communications. We have a service-manual-derived understanding of memory regions (basecode vs assay configuration) and the DB25 serial/parallel pinouts, but serial settings and the command/protocol remain unknown. Next steps are to confirm cabling (straight vs null-modem), determine serial parameters, and capture the first read-only responses from the instrument for protocol inference.

- **Project Goal:** Modern host-side control + data retrieval software for a BioTek ELx808 (and possibly multiple revisions).

- **Intermediate Goal:** Establish robust RS-232 communication and infer/document the instrument protocol (commands, framing, data formats).

- **Current Task:** Use the DB25 serial pinout to validate wiring and discover serial settings; begin safe read-only probing/logging.
