import pytest


@pytest.fixture
def my_settings():
    """Return settings in a conftest.py."""
    print(f"\nmy_settings fixture in {__file__}")
    return {"name": "Eric"}
