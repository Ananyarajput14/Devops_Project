import pytest
from app.utils import add_numbers, divide_numbers

def test_add_numbers():
    assert add_numbers(3, 2) == 5

def test_divide_numbers():
    assert divide_numbers(10, 2) == 5

def test_divide_by_zero():
    try:
        divide_numbers(5, 0)
    except ValueError as e:
        assert str(e) == "Division by zero is not allowed"
