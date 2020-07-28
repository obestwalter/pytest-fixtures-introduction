"""If I don't depend on a fixture object, I can declare this differently."""
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
    """Fool the program into using a different environment for the settings."""
    monkeypatch.setattr(my_code, "MY_SETTINGS_PATH", tmp_path / ".my_fake_settings")
    print(f"\nfake_settings_environment fixture in {__file__} -> {tmp_path}")


@pytest.mark.usefixtures("fake_settings_environment")
def test_read_my_settings(my_settings):
    """Make sure that settings are read correctly."""
    my_code.MY_SETTINGS_PATH.write_text(json.dumps(my_settings))
    assert my_code.read_my_settings() == my_settings


@pytest.mark.usefixtures("fake_settings_environment")
def test_write_my_settings(my_settings):
    """Make sure that settings are written correctly."""
    my_code.write_my_settings(my_settings)
    retrieved_settings = eval(my_code.MY_SETTINGS_PATH.read_text())
    assert retrieved_settings == my_settings
