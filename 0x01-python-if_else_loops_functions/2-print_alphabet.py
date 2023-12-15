#!/usr/bin/python3

def print_lowercase_alphabet():
    """
    Prints the lowercase alphabet characters.

    This function prints the lowercase alphabet characters
    in the range from 'a' to 'z'.

    Returns:
        None
    """
    for character in range(97, 123):
        print("{:c}".format(character), end='')

if __name__ == "__main__":
    # Call the function to print the lowercase alphabet
    print_lowercase_alphabet()

