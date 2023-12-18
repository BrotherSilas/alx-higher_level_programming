#!/usr/bin/python3

# -----------------------------------------------------------
# Python function that demonstrates how to print numbers from 0 to 99
#
# (C) 2023, Silas Edet, Uyo, Nigeria
# email: silasedetsnr@gmail.com
# -----------------------------------------------------------

for number in range(0, 99):

    print("{:02d}".format(number), end=", ")

print(99)
