"""Parametrizing tests means that fixtures are created on the fly.

Interesting command line options

pytest --fixtures           # shows all available fixtures
pytest --fixtures-per-test  # shows which fixtures are used per test
pytest --setup-plan         # only show what would be done
pytest --setup-only         # run the fixtures but not the tests
pytest --setup-show         # run tests and show fixture setup/teardown

e.g. set Edit Configurations -> Additional Arguments: --setup-show
"""
import pytest


@pytest.mark.parametrize(
    'first_number, next_number',
    (
        (1, 2),
        (3, 4),
        (5, 7),
    )
)
def test_params_are_fixtures(first_number, next_number):
    assert first_number + 1 == next_number
