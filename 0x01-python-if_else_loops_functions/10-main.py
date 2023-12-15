#!/usr/bin/env python3

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
    result1 = add(1, 2)
    result2 = add(98, 0)
    result3 = add(100, -2)

    # Print the results
    print(result1)
    print(result2)
    print(result3)

