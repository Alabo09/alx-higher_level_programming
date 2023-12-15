#!/usr/bin/python3
import random

def check_number_positivity(number):
    """
    Checks the positivity of a given number.

    Args:
        number (int): The number to be checked.

    Returns:
        str: A string indicating if the number is positive, zero, or negative.
    """
    if number > 0:
        return "{} is positive".format(number)
    elif number == 0:
        return "{} is zero".format(number)
    elif number < 0:
        return "{} is negative".format(number)

if __name__ == "__main__":
    # Generate a random number between -10 and 10
    number = random.randint(-10, 10)

    # Check and print the positivity of the generated number
    result = check_number_positivity(number)
    print(result)
