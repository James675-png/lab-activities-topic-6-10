# Topic8_4_c3.py
# Pytest test for invalid scores in the letter_grade() function.

import pytest
from grading import letter_grade


def test_score_above_100_raises_error():
    # Verify that a score above 100 raises a ValueError
    with pytest.raises(ValueError):
        letter_grade(150)