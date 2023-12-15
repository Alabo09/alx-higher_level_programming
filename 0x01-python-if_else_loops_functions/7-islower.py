#!/usr/bin/python3

def is_lower_case(c):
    """
    Checks if a given character is a lowercase letter.

    Args:
        c (str): The character to be checked.

    Returns:
        bool: True if the character is a lowercase letter, False otherwise.
    """
    if ord(c) > 96:
        return True
    else:
        return False

