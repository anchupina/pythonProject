# test_assert.py
import sys

import pytest


def login():
    return 42


def test_function():
    assert login() == 41


# division by zero pytest.raises
def test_exception():
    with pytest.raises(Exception) as excinfo:
        x = 1 / 0
    print(f'Exception text: {str(excinfo.value)}')


@pytest.mark.skip(reason="empty_test")
def test_skip_example():
    pass


@pytest.mark.skipif(sys.platform == 'win32', reason="only unix")
def test_skip_example():
    unix_logic()


@pytest.mark.xfail(
    strict=True,
    reason='wait for fix',


raise=TimeoutError,
run = True
)

def test_function():
    logic()


@pytest.mark.parametrize(
    "x, y, expected,", [
        (3, 8, 11),
        (5, 7, 12)
    ]
)
def test_addition(x, y, expected):
    assert x + y == expected

