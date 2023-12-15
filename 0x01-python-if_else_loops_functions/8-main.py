#!/usr/bin/env python3

def uppercase(s):
    """
    Prints a string in uppercase.

    Args:
        s (str): The input string.

    Returns:
        None
    """
    for char in s:
        # Convert each character to uppercase using the ord() and chr() functions
        print(chr(ord(char) - 32) if ord(char) >= 97 and ord(char) <= 122 else char, end='')
    print()  # Print a newline at the end

if __name__ == "__main__":
    # Importing uppercase from the module
    uppercase = __import__('8-uppercase').uppercase

    # Test cases
    uppercase("holberton")
    uppercase("Holberton School 98 Battery street")

