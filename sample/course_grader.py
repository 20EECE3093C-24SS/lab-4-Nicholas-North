# TODO-1: add convert_to_letter_grade(score) function
    
def convert_to_letter_grade(score):
    """Function that returns Capital letter grade for input
    int or float score value

    Args:
        score: int or float value for score

    Returns:
        Capital letter corresponding to letter grade. Can be
        anything from {A, B, C, D, F}

    """
    if not isinstance(score, (int, float)):
        raise TypeError(“Score must be a numeric value.”)

    if score < 0 or score > 100:
        raise ValueError(“Score must be between 0 and 100.”)

    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
