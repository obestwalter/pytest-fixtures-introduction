"""Writing a simple custom fixture.

PyCharm understands pytest

* fixture completion
* fixture navigation
* no false positive warning that the module level fixture name shadows the parameter
* visually debug tests just as normal code
"""
import json

import pytest

from my_package import my_code


@pytest.fixture
def my_settings():
    """Return settings in a specific test module."""
    print(f"\nmy_settings fixture in {__file__}")
    return {"name": "Eric"}


# FIXME PyCharm bug? If I navigate to my_settings it ends up in conftest.py ...
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
