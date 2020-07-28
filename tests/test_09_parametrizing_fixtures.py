"""Parametrizing fixtures / Fixtures depending on fixtures.

When a fixture is parametrized this parametrizes all depending tests

You can use other fixtures from fixtures.
"""
import json

import pytest

from my_package import my_code


@pytest.fixture(params=("Eric", "Brüno"))
def my_settings(request):
    """Create more tests from all functions using this fixture.

    The request fixture is needed for that

    https://docs.pytest.org/en/stable/reference.html?#request
    """
    print(f"parametrized my_settings: {request.param}")
    return {"name": request.param}


def test_read_my_settings(monkeypatch, tmp_path, my_settings):
    """Make sure that settings are read correctly."""
    monkeypatch.setattr(my_code, "MY_SETTINGS_PATH", tmp_path / ".my_fake_settings")
    my_code.MY_SETTINGS_PATH.write_text(json.dumps(my_settings))
    assert my_code.read_my_settings() == my_settings


def test_write_my_settings(monkeypatch, tmp_path, my_settings):
    """Make sure that settings are written correctly."""
    monkeypatch.setattr(my_code, "MY_SETTINGS_PATH", tmp_path / ".my_fake_settings")
    my_code.write_my_settings(my_settings)
    retrieved_settings = eval(my_code.MY_SETTINGS_PATH.read_text())
    assert retrieved_settings == my_settings
