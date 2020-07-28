"""The same tests using builtin fixtures.

Important command line options when working with fixtures

pytest --fixtures           # shows all available fixtures in current test suite
pytest --fixtures-per-test  # shows which fixtures are used per test
pytest --setup-plan         # only show what would be done
pytest --setup-only         # run the fixtures but not the tests
pytest --setup-show         # run tests and show fixture setup/teardown

(to use in PyCharm) set Edit Configurations -> Additional Arguments: --setup-show
"""
import json

from my_package import my_code

MY_SETTINGS = {"name": "Eric"}


def test_read_my_settings(tmp_path, monkeypatch):
    """Make sure that settings are read correctly."""
    monkeypatch.setattr(my_code, "MY_SETTINGS_PATH", tmp_path / ".my_fake_settings")
    my_code.MY_SETTINGS_PATH.write_text(json.dumps(MY_SETTINGS))
    assert my_code.read_my_settings() == MY_SETTINGS


def test_write_my_settings(monkeypatch, tmp_path):  # <- order doesn't matter
    """Make sure that settings are written correctly."""
    monkeypatch.setattr(my_code, "MY_SETTINGS_PATH", tmp_path / ".my_fake_settings")
    my_code.write_my_settings(MY_SETTINGS)
    retrieved_settings = eval(my_code.MY_SETTINGS_PATH.read_text())
    assert retrieved_settings == MY_SETTINGS
