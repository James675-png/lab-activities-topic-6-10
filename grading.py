# grading.py
# Contains a reusable function for converting scores into letter grades.

def letter_grade(score):
    """Return the letter grade for a score.
    Raise ValueError if the score is outside 0 to 100.
    """
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")

    if score >= 80:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 40:
        return "C"
    else:
        return "F"