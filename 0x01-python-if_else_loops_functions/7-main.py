#!/usr/bin/env python3

def is_lower_case(c):
    """
    Checks if a given character is a lowercase letter.

    Args:
        c (str): The character to be checked.

    Returns:
        bool: True if the character is a lowercase letter, False otherwise.
    """
    return ord(c) >= 97 and ord(c) <= 122

if __name__ == "__main__":
    # Importing islower from the module
    islower = __import__('7-islower').islower

    # Test cases
    print("a is {}".format("lower" if islower("a") else "upper"))
    print("H is {}".format("lower" if islower("H") else "upper"))
    print("A is {}".format("lower" if islower("A") else "upper"))
    print("3 is {}".format("lower" if islower("3") else "upper"))
    print("g is {}".format("lower" if islower("g") else "upper"))

