# Topic8_4_c2.py
# Pytest tests for the letter_grade() function.

from grading import letter_grade


def test_boundary_39_40():
    # Verify the boundary between F and C
    assert letter_grade(39) == "F"
    assert letter_grade(40) == "C"


def test_boundary_59_60():
    # Verify the boundary between C and B
    assert letter_grade(59) == "C"
    assert letter_grade(60) == "B"


def test_boundary_79_80():
    # Verify the boundary between B and A
    assert letter_grade(79) == "B"
    assert letter_grade(80) == "A"
