# Pepkio RCF ↔ RPM Rotor Converter

Containerized CLI for RPM↔×g conversion, rotor protocol transfer, and batch spin-step processing via the Pepkio Tools API.

**Image status:** Published on Docker Hub as `pepkio/rcf-rpm-rotor-converter:0.1.0` (https://hub.docker.com/r/pepkio/rcf-rpm-rotor-converter).

# What It Does

This image runs the `pepkio-rcf-rpm-rotor-converter` CLI against the hosted API backend. It supports manifest discovery, RPM↔RCF conversion with tri-radius output, protocol transfer between rotors, and batch CSV conversion using the same input structure as the web tool.

Use it when you want a reproducible runtime in CI jobs, shared servers, or scripted command-line workflows without installing Python dependencies directly on the host.

# Features

- CLI commands for `manifest` and `run`
- Manifest example execution (`--example`)
- JSON input execution (`--input-json`)
- API base URL override for environment switching
- Structured run responses with `run_id`, `status`, and `result`
- Modes: `convert`, `transfer`, `batch`

# Quick Start

```bash
docker pull pepkio/rcf-rpm-rotor-converter:0.1.0
docker run --rm -it pepkio/rcf-rpm-rotor-converter:0.1.0
```

Run a manifest example:

```bash
docker run --rm \
  -e PEPKIO_API_KEY="YOUR_PEPKIO_API_KEY" \
  pepkio/rcf-rpm-rotor-converter:0.1.0 \
  pepkio-rcf-rpm-rotor-converter run --example rpm_to_rcf_10k
```

# Quick Example

```bash
docker run --rm \
  -e PEPKIO_API_KEY="YOUR_PEPKIO_API_KEY" \
  pepkio/rcf-rpm-rotor-converter:0.1.0 \
  pepkio-rcf-rpm-rotor-converter run --input-json '{"mode":"convert","direction":"rpm_to_rcf","speed":10000,"rmin_mm":50,"ravg_mm":55,"rmax_mm":60}'
```

# Typical Use Cases

- Converting RPM to ×g in containerized CI smoke tests
- Validating protocol transfer calculations in reproducible jobs
- Batch-processing centrifuge protocol CSV rows in automation scripts
- Reusing manifest examples as integration tests without a local Python install

# Scientific Background

RCF (×g) depends on RPM and rotor radius: RCF = 1.118 × 10⁻⁵ × r(cm) × RPM². The tool returns g-force at rmin, ravg, and rmax; transfer mode matches rmax RCF when moving a spin step between rotors.

# Web Application

For researchers who prefer a graphical interface, an interactive web version is available.

Web Application: https://www.pepkio.com/tools/rcf-rpm-rotor-converter

The web interface offers searchable rotor presets, tri-radius display, shareable links, and printable records.

# Documentation and Resources

GitHub Repository: https://github.com/pepkio/pepkio-rcf-rpm-rotor-converter

Web Application: https://www.pepkio.com/tools/rcf-rpm-rotor-converter

Source and Dockerfile: https://github.com/pepkio/pepkio-rcf-rpm-rotor-converter

# About Pepkio

Pepkio (https://www.pepkio.com/) develops software tools and bioinformatics solutions for life science researchers, including laboratory calculators and analysis services (https://www.pepkio.com/cro).
