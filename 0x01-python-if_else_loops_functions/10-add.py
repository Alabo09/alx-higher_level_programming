#!/usr/bin/python3

def add(a, b):
    """
    Adds two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two input numbers.
    """
    return a + b

if __name__ == "__main__":
    # Test cases
    result = add(5, 10)
    print("Result: {}".format(result))

