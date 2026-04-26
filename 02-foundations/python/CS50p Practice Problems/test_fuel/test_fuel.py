import pytest
from fuel import convert, gauge

def test_convert():
    # Test valid conversions
    assert convert("1/2") == 50
    assert convert("0/1") == 0
    assert convert("1/1") == 100

    # Test ValueError for non-integers or X > Y
    with pytest.raises(ValueError):
        convert("cat/dog")
        convert("5/4")

    # FIX: Add specific checks for negative fractions
    with pytest.raises(ValueError):
        convert("-1/3")
    with pytest.raises(ValueError):
        convert("1/-3")

    # Test ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
