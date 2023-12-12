#!/usr/bin/python3
# -----------------------------------------------------------
# -----------------------------------------------------------
# Python function that replaces all occurrences of an element by another in a new list.
#
# (C) 2023, Silas Edet, Uyo, Nigeria
# email: silasedetsnr@gmail.com
# -----------------------------------------------------------

def search_replace(my_list, search, replace):
    new_list = []
    for x in my_list:
        if x != search:
            new_list.append(x)
        else:
            new_list.append(replace)
    return new_list
