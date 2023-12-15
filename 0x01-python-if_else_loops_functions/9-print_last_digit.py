#!/usr/bin/env python3

def print_last_digit(number):
    """
    Prints the last digit of a given number.

    Args:
        number (int): The input number.

    Returns:
        int: The last digit of the input number.
    """
    last_digit = abs(number) % 10  # Calculate the last digit using the modulo operator
    print("{:d}".format(last_digit))
    return last_digit

if __name__ == "__main__":
    # Test cases
    print_last_digit(98)
    print_last_digit(0)
    r = print_last_digit(-1024)
    print(r)

