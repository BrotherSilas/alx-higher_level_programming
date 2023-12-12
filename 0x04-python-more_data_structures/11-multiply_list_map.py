#!/usr/bin/python3
# -----------------------------------------------------------
# Python function that demonstrates how to return a list with all values multiplied by a number
#
# (C) 2023, Silas Edet, Uyo, Nigeria
# email: silasedetsnr@gmail.com
# -----------------------------------------------------------

def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: number * x, my_list))
