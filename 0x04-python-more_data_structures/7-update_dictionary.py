#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that replaces or adds key/value in a dictionary.
#
# (C) 2023, Silas Edet, Uyo, Nigeria
# email: silasedetsnr@gmail.com
# -----------------------------------------------------------

def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary[key] = value
    else:
        for x in a_dictionary:
            if x == key:
                a_dictionary[x] = value
    return a_dictionary
