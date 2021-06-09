from math_series import __version__
from math_series.series import fibonacci, lucas, sum_series


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
    actual = lucas(4)
    expected = 4
    assert actual == expected

def test_lucas_eight():
    actual = lucas(8)
    expected = 29
    assert actual == expected

def test_sum_series_fib_four():
    actual = sum_series(4)
    expected = 2
    assert actual == expected

def test_sum_series_fib_eight():
    actual = sum_series(8)
    expected = 13
    assert actual == expected

def test_sum_series_lucas_four():
    actual = sum_series(4, 2, 1)
    expected = 4
    assert actual == expected

def test_sum_series_lucas_eight():
    actual = sum_series(8, 2, 1)
    expected = 29
    assert actual == expected

def test_sum_series_evens_four():
    actual = sum_series(4, 2, 4)
    expected = 10
    assert actual == expected

def test_sum_series_evens_eight():
    actual = sum_series(8, 2, 4)
    expected = 68
    assert actual == expected