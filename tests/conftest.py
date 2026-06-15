"""Pytest fixtures."""

from __future__ import annotations

from pathlib import Path

import pytest
from dotenv import load_dotenv

# Load monorepo .env for local integration runs (never log keys).
_monorepo_env = Path(__file__).resolve().parents[3] / ".env"
if _monorepo_env.is_file():
    load_dotenv(_monorepo_env)

_package_env = Path(__file__).resolve().parents[1] / ".env"
if _package_env.is_file():
    load_dotenv(_package_env)


@pytest.fixture
def mock_manifest() -> dict:
    return {
        "tool_id": "rcf-rpm-rotor-converter",
        "title": "RCF ↔ RPM Rotor Converter",
        "execution_mode": "sync",
        "examples": [
            {
                "name": "rpm_to_rcf_10k",
                "input": {
                    "mode": "convert",
                    "direction": "rpm_to_rcf",
                    "speed": 10000,
                    "rmin_mm": 50,
                    "ravg_mm": 55,
                    "rmax_mm": 60,
                },
            },
            {
                "name": "rcf_to_rpm_5k",
                "input": {
                    "mode": "convert",
                    "direction": "rcf_to_rpm",
                    "speed": 5000,
                    "rmin_mm": 50,
                    "ravg_mm": 55,
                    "rmax_mm": 60,
                },
            },
        ],
    }


@pytest.fixture
def mock_run_response() -> dict:
    return {
        "run_id": "run_test123",
        "status": "completed",
        "result": {
            "mode": "convert",
            "result": {
                "rcf": {
                    "rmin_rcf": 5590,
                    "ravg_rcf": 6149,
                    "rmax_rcf": 6708,
                }
            },
        },
        "error": None,
        "result_url": "https://tools.pepkio.com/api/tools/v1/runs/run_test123",
        "permalink": "https://tools.pepkio.com/r/run_test123",
    }
