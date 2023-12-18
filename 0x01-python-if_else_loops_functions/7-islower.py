#!/usr/bin/python3

# -----------------------------------------------------------
# Python function that demonstrates how to check for lowercase character using ASCII code
# islower: function Checks for lowercase
# Args c: a single character argument
#
# Returns: True,if c is lowercase and False, if c is not lowercase
# (C) 2023, Silas Edet, Uyo, Nigeria
# email: silasedetsnr@gmail.com
# -----------------------------------------------------------

def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    return False
