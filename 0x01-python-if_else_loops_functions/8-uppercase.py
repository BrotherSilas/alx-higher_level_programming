#!/usr/bin/python3

# -----------------------------------------------------------
# Python function that demonstrates how to print a string in uppercase
#
# (C) 2023, Silas Edet, Uyo, Nigeria
# email: silasedetsnr@gmail.com
# -----------------------------------------------------------

def uppercase(str):
    """Prints uppercase string

    Args:
        str: a character string argument
    """

    for letter in str:

        ascii_letter_code = ord(letter)

        if ascii_letter_code in range(97, 123):

            ascii_letter_code = ascii_letter_code - 32

        print("{:c}".format(ascii_letter_code), end="")
    print()
