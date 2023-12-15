#!/usr/bin/python3

def print_decimal_and_hexadecimal():
    """
    Prints the decimal and hexadecimal representation of numbers.

    This function prints the numbers from 0 to 98 along with their
    decimal and hexadecimal representation in the format "{decimal} = 0x{hex}".

    Returns:
        None
    """
    for num in range(0, 99):
        print("{:d} = 0x{:x}".format(num, num))

if __name__ == "__main__":
    # Call the function to print decimal and hexadecimal representations
    print_decimal_and_hexadecimal()

