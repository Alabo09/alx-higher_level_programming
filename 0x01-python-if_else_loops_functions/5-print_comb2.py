#!/usr/bin/python3

def print_padded_numbers():
    """
    Prints padded numbers from 00 to 99.

    This function prints numbers from 00 to 99 in a padded format
    using the format specifier "{:02d}" and separated by commas.

    Returns:
        None
    """
    for num in range(00, 100):
        # Print the padded number followed by a comma, except for the last number
        print("{:02d}".format(num), end='\n' if num == 99 else ", ")

if __name__ == "__main__":
    # Call the function to print padded numbers
    print_padded_numbers()

