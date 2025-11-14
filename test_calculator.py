import pytest
from calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_subtract():
    calc = Calculator()
    assert calc.subtract(10, 4) == 6

def test_multiply():
    calc = Calculator()
    assert calc.multiply(3, 5) == 15

def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(10, 0)

def test_average():
    calc = Calculator()
    assert calc.average([2, 4, 6, 8]) == 5

def test_average_empty_list():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.average([])
