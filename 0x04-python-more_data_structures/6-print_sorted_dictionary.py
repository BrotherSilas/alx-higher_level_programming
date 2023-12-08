#!/usr/bin/python3
# -----------------------------------------------------------
# Python function that that prints a dictionary by ordered keys.
#
# (C) 2023, Silas Edet, Uyo, Nigeria
# email: silasedetsnr@gmail.com
# -----------------------------------------------------------

def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary):
        print(f"{key}: {a_dictionary[key]}")
