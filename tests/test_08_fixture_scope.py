"""Fixture scope.

Maybe lifetime would be a better term? But scope is the official name of the kwarg

Available scopes:
* function (default)
* class
* module
* package (experimental - finalized when last test of a package finishes)
* session

and the new dynamic scope: https://docs.pytest.org/en/stable/fixture.html?#dynamic-scope

monkeypatch has function scope
"""
import json

import pytest

from my_package import my_code


@pytest.fixture(scope="session")
def my_settings():
    """Return settings in a test module with session scope."""
    print(f"\nmy_settings fixture in {__file__}")
    return {"name": "Eric"}


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
