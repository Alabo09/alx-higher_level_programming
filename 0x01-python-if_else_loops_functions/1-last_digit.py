#!/usr/bin/python3
import random

def determine_last_digit(number):
    """
    Determines the last digit of a given number.

    Args:
        number (int): The number for which to determine the last digit.

    Returns:
        int: The last digit of the given number.
    """
    if number >= 0:
        return number % 10
    else:
        return ((number * -1) % 10) * -1

if __name__ == "__main__":
    # Generate a random number between -10000 and 10000
    number = random.randint(-10000, 10000)

    # Determine the last digit of the generated number
    last_digit = determine_last_digit(number)

    # Compose a message about the last digit
    message = "Last digit of %d is %d and is" % (number, last_digit)

    # Check and print conditions based on the last digit
    if last_digit == 0:
        print(message, "0")
    elif last_digit > 5:
        print(message, "greater than 5")
    else:
        print(message, "less than 6 and not 0")

