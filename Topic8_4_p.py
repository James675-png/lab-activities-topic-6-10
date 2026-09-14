# Topic8_4_p.py
# Pytest tests for the validate_age() function.

import pytest
from validators import validate_age


def test_valid_age():
    # Verify that a typical valid age passes
    assert validate_age(25) is True


def test_boundary_age_120():
    # Verify that the upper boundary value is valid
    assert validate_age(120) is True


def test_invalid_age_raises_error():
    # Verify that an age above 120 raises ValueError
    with pytest.raises(ValueError):
        validate_age(121)