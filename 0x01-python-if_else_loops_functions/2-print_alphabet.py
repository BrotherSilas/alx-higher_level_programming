#!/usr/bin/python3

# -----------------------------------------------------------
# Python function demonstrates how to print the ASCII alphabet in lowercase
#
# (C) 2023, Silas Edet, Uyo, Nigeria
# email: silasedetsnr@gmail.com
# -----------------------------------------------------------

for ascii_code in range(97, 123):

    # Print out the character format of the ascii_code
    print("{:c}".format(ascii_code), end='')
