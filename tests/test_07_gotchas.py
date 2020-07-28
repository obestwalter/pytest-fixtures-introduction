"""How to shoot yourself in the foot with pytest.

Interesting bugs are usually an unfortunate combination of wrong assumptions playing
together in a way that it might seem like things work fine on first look but they don't

* check your assumptions, especially when dealing with test code (test your tests?)
* use assertions to verify important assumptions programmatically, also in fixtures/tests
* if something goes wrong in a fixture, this is an error -  not a test failure
"""
import tempfile

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


# name doesn't shadow fixture above (but it does shadow the one in conftest.py)
# I'm not sure about the implementation - it might be random which one wins
@pytest.fixture(name="my_settings")
# we think we use the fake_settings_environment fixture but we don't
@pytest.mark.usefixtures("fake_settings_environment")  # this fails silently :(
def kitchensink(my_settings):
    assert tempfile.gettempdir() in str(
        my_code.MY_SETTINGS_PATH
    ), my_code.MY_SETTINGS_PATH
    return my_settings


def test_forgot_a_dependency():
    # easy to debug, but something static code analysis won't catch
    # as PyCharm is pytest aware it **could** catch something like this though ...
    assert my_settings == {"name": "Eric"}


def test_using_my_settings(my_settings):
    # TODO comment out to show bug
    # assert tempfile.gettempdir() in str(
    #     my_code.MY_SETTINGS_PATH
    # ), my_code.MY_SETTINGS_PATH
    assert my_settings == {"name": "Eric"}


@pytest.mark.usefixtures("kitchensink")
def test_using_kitchensink(my_settings):
    # kitchensink fixture doesn't exist when a name is explicitly set
    assert tempfile.gettempdir() in str(
        my_code.MY_SETTINGS_PATH
    ), my_code.MY_SETTINGS_PATH
    assert my_settings == {"name": "Eric"}
