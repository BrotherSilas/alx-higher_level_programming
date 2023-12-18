#!/usr/bin/python3

# -----------------------------------------------------------
# Python function that demonstrates how to print the ASCII alphabet in lowercase except 'q' and 'e'
#
# (C) 2023, Silas Edet, Uyo, Nigeria
# email: silasedetsnr@gmail.com
# -----------------------------------------------------------

for ascii_code in range(97, 123):

    if ascii_code == 101 or ascii_code == 113:
        continue

    print("{:c}".format(ascii_code), end='')
