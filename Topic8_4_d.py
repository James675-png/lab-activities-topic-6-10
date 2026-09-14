# Topic8_4_d.py
# Pytest test cases for the functions defined in calculator.py

import pytest
from calculator import add, divide, multiply


def test_add_positive_numbers():
    # Verify that adding two positive numbers returns the correct sum
    assert add(2, 3) == 5


def test_add_negative_numbers():
    # Verify that adding two negative numbers returns the correct sum
    assert add(-2, -3) == -5


def test_divide_normal_case():
    # Verify that division returns the correct quotient
    assert divide(10, 2) == 5


def test_divide_by_zero_raises_error():
    # Verify that dividing by zero raises a ValueError
    with pytest.raises(ValueError):
        divide(10, 0)

def test_add_zero_numbers():
    # Verify that adding zero and zero returns zero
    assert add(0, 0) == 0

def test_multiply_numbers():
    # Verify that multiplying two numbers returns the correct product
    assert multiply(4, 5) == 20
