#!/usr/bin/python3
# -----------------------------------------------------------
# Python function that demonstrates how to delete keys with a specific value in a dictionary
#
# (C) 2023, Silas Edet, Uyo, Nigeria
# email: silasedetsnr@gmail.com
# -----------------------------------------------------------

def complex_delete(a_dictionary, value):
    for index in list(a_dictionary.keys()):
        if a_dictionary[index] == value:
            del a_dictionary[index]
    return a_dictionary
