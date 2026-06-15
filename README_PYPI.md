# Pepkio RCF ↔ RPM Rotor Converter

Call the Pepkio `rcf-rpm-rotor-converter` REST API from Python to convert RPM↔×g with tri-radius output, transfer spin steps between rotors, and batch-process protocol CSV rows.

# What It Does

Published centrifuge protocols cite RPM or ×g, but the conversion depends on rotor geometry. Rebuilding RCF math and rotor-radius lookups in a notebook for each protocol is slow and error-prone.

This package submits conversion, transfer, and batch inputs to the same Pepkio Tools engine as the hosted web calculator. It returns tri-radius RCF or RPM values, optional max-RPM warnings, methods-ready text, and shareable run permalinks.

Programmatic runs require a network connection and a Pepkio API key. Calculations are not bundled for offline use.

# Features

- Modes: `convert`, `transfer`, `batch`
- Convert directions: `rpm_to_rcf`, `rcf_to_rpm` with rmin, ravg, rmax output (mm)
- Rotor presets via `rotor_id` (for example `beckman-ja-20`, `eppendorf-fa-45-24-11`)
- Protocol transfer: source RPM on one rotor → target RPM on another at matched rmax RCF
- Batch CSV: columns `label,direction,speed,rmin,ravg,rmax,rotor_id`
- Manifest examples: `rpm_to_rcf_10k`, `rcf_to_rpm_5k`, `transfer_ja20_to_eppendorf`, `batch_two_rows`, `rotor_id_only_ja20`
- CLI: `pepkio-rcf-rpm-rotor-converter manifest` and `run`
- Configuration via `PEPKIO_API_KEY`, `LOCAL_PEPKIO_API_KEY`, and `PEPKIO_API_BASE_URL`

# Installation

```bash
pip install pepkio-rcf-rpm-rotor-converter
```

Set an API key with **tools:run** scope before calling `run()`:

```bash
export PEPKIO_API_KEY="your-key"
```

Create a key in your [Pepkio account API keys](https://www.pepkio.com/account/api-keys) settings.

# Quick Example

```python
from pepkio_rcf_rpm_rotor_converter import PepkioClient

with PepkioClient() as client:
    inp = client.get_example_input("rpm_to_rcf_10k")
    result = client.run(inp)
    print(result.result["result"]["rcf"])  # rmin_rcf, ravg_rcf, rmax_rcf
```

CLI:

```bash
pepkio-rcf-rpm-rotor-converter run --example rpm_to_rcf_10k
```

Manifest inspection does not require an API key.

# Typical Use Cases

- Converting protocol RPM to ×g for methods sections
- Matching a published ×g target on your rotor by solving for RPM at rmax
- Transferring spin steps between Beckman and Eppendorf rotors
- Batch-converting multi-step centrifuge protocols from CSV
- Validating manifest examples in CI or notebook workflows

# Scientific Background

RCF (×g) relates to RPM and radius: RCF = 1.118 × 10⁻⁵ × r(cm) × RPM². This tool reports g-force at rmin, ravg, and rmax simultaneously; pelleting protocols often reference rmax RCF because sediment collects at the tube bottom.

# Web Application

For researchers who prefer a graphical interface, an interactive web version is available.

Web Application: https://www.pepkio.com/tools/rcf-rpm-rotor-converter

The web interface offers searchable rotor presets, a tube force-gradient diagram, shareable links, browser history, and printable records.

# Documentation and Resources

GitHub Repository: https://github.com/pepkio/pepkio-rcf-rpm-rotor-converter

Web Application: https://www.pepkio.com/tools/rcf-rpm-rotor-converter

Source and issues: https://github.com/pepkio/pepkio-rcf-rpm-rotor-converter

# About Pepkio

Pepkio develops software tools and provides bioinformatics analysis services for life science research. See https://www.pepkio.com for additional tools and services, including laboratory calculators and analysis services at https://www.pepkio.com/cro.

# Keywords

RCF RPM converter, centrifuge RPM to ×g, relative centrifugal force, rotor radius mm, tri-radius output, protocol transfer, batch CSV centrifuge, Beckman JA-20, Eppendorf rotor, pepkio-rcf-rpm-rotor-converter, Python centrifuge client, laboratory calculator, REST API, convert rpm_to_rcf rcf_to_rpm, max RPM warning, methods text centrifuge, how to convert RPM to RCF Python API, transfer centrifuge protocol between rotors programmatically, batch convert spin steps CSV Pepkio, calculate rmax g force from RPM script, equivalent RPM different rotor same RCF API
