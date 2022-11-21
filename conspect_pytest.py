import pytest


@pytest.mark.parametrize(
    "x, y, expected,", [
        (3, 8, 11),
        (5, 7, 12)
    ]
)
def test_addition(x, y, expected):
    assert x + y == expected