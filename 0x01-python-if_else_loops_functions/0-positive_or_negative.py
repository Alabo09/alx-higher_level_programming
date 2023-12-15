#!/usr/bin/python3
import random


def check_positive_negative_zero(number):
    """
    This function checks if a number is positive, negative, or zero.

    Args:
        number (int): The number to be checked.

    Returns:
        None
    """
    if number > 0:
        print("{} is positive".format(number))
    elif number == 0:
        print("{} is zero".format(number))
    elif number < 0:
        print("{} is negative".format(number))


# Generate a random number between -10 and 10
random_number = random.randint(-10, 10)

# Call the function to check the generated number
check_positive_negative_zero(random_number)
)
