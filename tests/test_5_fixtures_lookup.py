"""Fixture lookup / discovery

What LEGB is for Python names, CMLIB is for pytest fixtures

... only not as palatable

* (C)lass
* (M)odule
* (L)ocal plugins (conftest.py - searching directory upwards)
* (I)nstalled plugins
* (B)uiltin fixtures
"""
import json

import pytest

from my_package import my_code

# my_settings was removed so the one in conftest.py is found now


@pytest.fixture
def tmp_path():
    """A self made tmp_path fixture, that is found first in this module."""
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as tmp_dirname:
        print(f"\ntmp_path fixture in {__file__}")
        yield Path(tmp_dirname)


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
