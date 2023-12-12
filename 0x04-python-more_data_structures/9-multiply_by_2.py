#!/usr/bin/python3
# -----------------------------------------------------------
# Python function that returns a new dictionary with all values multiplied by 2
#
# (C) 2023, Silas Edet, Uyo, Nigeria
# email: silasedetsnr@gmail.com
# -----------------------------------------------------------

def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for key, value in new_dict.items():
        new_dict[key] = value * 2
    return new_dict
