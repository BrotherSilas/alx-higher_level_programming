#!/usr/bin/python3

# -----------------------------------------------------------
# Python function that demonstrates how to print the smallest, unique combinations of two digits
#
# (C) 2023, Silas Edet, Uyo, Nigeria
# email: silasedetsnr@gmail.com
# -----------------------------------------------------------

for first_digit in range(0, 8):
    for second_digit in range(0, 10):
        if not (second_digit <= first_digit):
            print("{:d}{:d}".format(first_digit, second_digit), end=", ")

print("89")
