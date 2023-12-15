#!/usr/bin/python3

def fizz_buzz():
    """
    Implements the FizzBuzz algorithm for numbers 1 to 100.

    Prints:
        - "Fizz" for multiples of 3
        - "Buzz" for multiples of 5
        - "FizzBuzz" for multiples of both 3 and 5
        - The number itself for all other cases.

    Returns:
        None
    """
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz ", end="")
        elif i % 3 == 0:
            print("Fizz ", end="")
        elif i % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{:d} ".format(i), end="")

if __name__ == "__main__":
    # Call the fizz_buzz function to print FizzBuzz for numbers 1 to 100
    fizz_buzz()

