# Topic8_4_c1.py
# Pytest tests for the is_palindrome() function.

from string_ops import is_palindrome


def test_palindrome():
    # Verify that a palindrome returns True
    assert is_palindrome("Level") is True


def test_non_palindrome():
    # Verify that a non-palindrome returns False
    assert is_palindrome("Python") is False
