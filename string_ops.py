# string_ops.py
# Contains reusable string utility functions.

def is_palindrome(text):
    """Return True if the text is a palindrome, ignoring case."""
    text = text.lower()
    return text == text[::-1]
