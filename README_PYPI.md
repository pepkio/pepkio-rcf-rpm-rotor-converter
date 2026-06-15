# Pepkio RCF ↔ RPM Rotor Converter

Python client for the Pepkio `rcf-rpm-rotor-converter` tool (RPM/RCF conversion, rotor transfer, and batch CSV).

## Install

```bash
pip install pepkio-rcf-rpm-rotor-converter
```

## Quick start

```python
from pepkio_rcf_rpm_rotor_converter import PepkioClient

with PepkioClient() as client:
    result = client.run(client.get_example_input("rpm_to_rcf_10k"))
    print(result.result)
```

Web tool: https://www.pepkio.com/tools/rcf-rpm-rotor-converter

## Publish to PyPI

```bash
source ~/.bash_profile   # loads POETRY_PYPI_TOKEN_PYPI
uv build
uv publish
```

Do not commit API keys or PyPI tokens.
