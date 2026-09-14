# calculator.py
# Contains user-defined functions that will be tested using Pytest.

def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def divide(a, b):
    """Return the quotient of two numbers. Raises ValueError if dividing by zero."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b
