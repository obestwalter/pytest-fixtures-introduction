"""Parametrizing tests means that fixtures are created on the fly."""
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
