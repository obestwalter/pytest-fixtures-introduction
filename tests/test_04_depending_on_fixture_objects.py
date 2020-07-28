"""Fixtures can depend on objects that other fixtures provide."""
import json

import pytest

from my_package import my_code


@pytest.fixture
def my_settings():
    """Return settings in a specific test module."""
    print(f"\nmy_settings fixture in {__file__}")
    return {"name": "Eric"}


@pytest.fixture
def fake_settings_environment(monkeypatch, tmp_path):
    monkeypatch.setattr(my_code, "MY_SETTINGS_PATH", tmp_path / ".my_fake_settings")
    print(f"\nfake_settings_environment fixture in {__file__} -> {tmp_path}")


def test_read_my_settings(fake_settings_environment, my_settings):
    """Make sure that settings are read correctly."""
    my_code.MY_SETTINGS_PATH.write_text(json.dumps(my_settings))
    assert my_code.read_my_settings() == my_settings


def test_write_my_settings(fake_settings_environment, my_settings):
    """Make sure that settings are written correctly."""
    my_code.write_my_settings(my_settings)
    retrieved_settings = eval(my_code.MY_SETTINGS_PATH.read_text())
    assert retrieved_settings == my_settings
