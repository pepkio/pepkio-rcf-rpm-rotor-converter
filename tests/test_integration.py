"""Integration tests against live Pepkio Tools API."""

from __future__ import annotations

import os

import pytest

from pepkio_rcf_rpm_rotor_converter.client import PepkioClient

# Local first, then production (param order).
ENVIRONMENTS = [
    ("local", "https://tools.localtest.me"),
    ("production", "https://tools.pepkio.com"),
]


def _api_key_for(base_url: str) -> str | None:
    if "localtest.me" in base_url:
        return os.getenv("LOCAL_PEPKIO_API_KEY")
    return os.getenv("PEPKIO_API_KEY")


@pytest.fixture(params=ENVIRONMENTS, ids=["local", "production"])
def live_client(request):
    env_name, base_url = request.param
    api_key = _api_key_for(base_url)
    if not api_key:
        pytest.skip(f"No API key for {env_name} (set LOCAL_PEPKIO_API_KEY or PEPKIO_API_KEY)")
    with PepkioClient(api_key=api_key, base_url=base_url) as client:
        yield client


def test_get_manifest(live_client: PepkioClient):
    manifest = live_client.get_manifest(refresh=True)
    assert manifest["tool_id"] == "rcf-rpm-rotor-converter"
    names = live_client.list_examples()
    assert "rpm_to_rcf_10k" in names


def test_run_rpm_to_rcf_10k(live_client: PepkioClient):
    inp = live_client.get_example_input("rpm_to_rcf_10k")
    result = live_client.run(inp)
    assert result.status == "completed"
    assert result.run_id
    assert result.permalink
    assert result.result is not None
    inner = result.result.get("result")
    assert isinstance(inner, dict)
    rcf = inner.get("rcf")
    assert isinstance(rcf, dict)
    assert rcf["rmax_rcf"] == pytest.approx(6708, abs=5)
    assert result.error is None


def test_run_rcf_to_rpm_5k(live_client: PepkioClient):
    inp = live_client.get_example_input("rcf_to_rpm_5k")
    result = live_client.run(inp)
    assert result.status == "completed"
    assert result.result is not None
    inner = result.result.get("result")
    assert isinstance(inner, dict)
    rpm = inner.get("rpm")
    assert isinstance(rpm, dict)
    assert rpm["rmax_rpm"] == pytest.approx(8634, abs=5)
    assert result.error is None


def test_run_transfer_ja20_to_eppendorf(live_client: PepkioClient):
    inp = live_client.get_example_input("transfer_ja20_to_eppendorf")
    result = live_client.run(inp)
    assert result.status == "completed"
    assert result.result is not None
    inner = result.result.get("result")
    assert isinstance(inner, dict)
    assert inner["target_rpm"] == pytest.approx(13607, abs=5)
    assert result.error is None


def test_run_rotor_id_only_ja20(live_client: PepkioClient):
    inp = live_client.get_example_input("rotor_id_only_ja20")
    result = live_client.run(inp)
    assert result.status == "completed"
    assert result.result is not None
    inner = result.result.get("result")
    assert isinstance(inner, dict)
    rcf = inner.get("rcf")
    assert isinstance(rcf, dict)
    assert rcf["rmax_rcf"] == pytest.approx(48298, abs=5)
    assert result.error is None


def test_run_batch_two_rows(live_client: PepkioClient):
    inp = live_client.get_example_input("batch_two_rows")
    result = live_client.run(inp)
    assert result.status == "completed"
    assert result.result is not None
    inner = result.result.get("result")
    assert isinstance(inner, dict)
    rows = inner.get("rows")
    assert isinstance(rows, list)
    assert len(rows) >= 2
    assert result.error is None
