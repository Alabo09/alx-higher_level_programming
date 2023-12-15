#!/usr/bin/python3

def print_incremented_numbers():
    """
    Prints incremented numbers from 0 to 89 with special conditions.

    This function prints numbers from 0 to 89 with the following conditions:
    - Increment by 1.
    - When the number is a multiple of 10, increment by an additional value.

    The numbers are formatted using the format specifier "{:02d}" and separated by commas.

    Returns:
        None
    """
    number = 0
    while number <= 89:
        # Increment by 1, and for multiples of 10, increment by additional value
        if number % 10 == 0:
            number += 1 + number // 10

        # Print the formatted number followed by a comma, except for the last number
        print("{:02d}".format(number), end='\n' if number == 89 else ", ")
        
        # Increment by 1 for the next iteration
        number += 1

if __name__ == "__main__":
    # Call the function to print incremented numbers
    print_incremented_numbers()

