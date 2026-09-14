# validators.py
# Contains validation functions for user input.

def validate_age(age):
    """Return True for ages from 0 to 120 inclusive.
    Raise ValueError for ages outside that range.
    """
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120.")

    return True