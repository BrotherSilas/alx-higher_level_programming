#!/usr/bin/python3

# -----------------------------------------------------------
# Python program that demonstrates how to print prints the ASCII alphabet, in reverse order
#
# (C) 2023, Silas Edet, Uyo, Nigeria
# email: silasedetsnr@gmail.com
# -----------------------------------------------------------

for ascii_code in range(122, 96, -1):

    if ascii_code % 2 == 1:

        ascii_code = ascii_code - 32

    print("{:c}".format(ascii_code), end="")
