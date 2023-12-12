#!/usr/bin/python3
# -----------------------------------------------------------
#Python function that adds all unique integers in a list (only once for each integer).
#
# (C) 2023, Silas Edet, Uyo, Nigeria
# email: silasedetsnr@gmail.com
# -----------------------------------------------------------

def uniq_add(my_list=[]):
    my_new_set = set(my_list)
    sum = 0
    for number in my_new_set:
        sum += number
    return sum
