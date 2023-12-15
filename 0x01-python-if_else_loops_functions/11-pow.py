#!/usr/bin/python3

def power(a, b):
    """
    Calculates the power of a number.

    Args:
        a (int): The base.
        b (int): The exponent.

    Returns:
        int: The result of raising the base to the exponent.
    """
    return a ** b

if __name__ == "__main__":
    # Test cases
    result1 = power(2, 3)
    result2 = power(5, 0)
    result3 = power(3, -2)

    # Print the results
    print(result1)
    print(result2)
    print(result3)

