#!/usr/bin/python3

def to_upper(character):
    """
    Converts a lowercase character to its uppercase equivalent.

    Args:
        character (str): The character to be converted.

    Returns:
        int: The ASCII value of the uppercase equivalent, or the original ASCII value if not a lowercase letter.
    """
    if ord(character) >= 97 and ord(character) <= 122:
        return ord(character) - 32
    else:
        return ord(character)

def uppercase(string):
    """
    Prints a string in uppercase.

    Args:
        string (str): The input string.

    Returns:
        None
    """
    string_new = ""
    for character in string:
        # Convert each character to uppercase using the to_upper function
        string_new += "%c" % to_upper(character)
    print("{:s}".format(string_new))

if __name__ == "__main__":
    # Test cases
    uppercase("holberton")
    uppercase("Holberton School 98 Battery street")

