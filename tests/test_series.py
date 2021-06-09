from math_series import __version__
from math_series.series import fibonacci
from math_series.series import lucas


def test_version():
    assert __version__ == '0.1.0'


def test_fib_four():
    actual = fibonacci(4)
    expected = 2
    assert actual == expected

def test_fib_eight():
    actual = fibonacci(8)
    expected = 13
    assert actual == expected

def test_lucas_four():
    actual = fibonacci(4)
    expected = 4
    assert actual == expected

def test_lucas_eight():
    actual = fibonacci(8)
    expected = 29
    assert actual == expected