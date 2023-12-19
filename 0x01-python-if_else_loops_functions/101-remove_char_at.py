#!/usr/bin/python3

# -----------------------------------------------------------
# Python function that  demonstrates how to create a copy of the string, removing the character at
# the position n
#
# (C) 2023, Silas Edet, Uyo, Nigeria
# email: silasedetsnr@gmail.com
# -----------------------------------------------------------

def remove_char_at(str, n):
    
    if n >= 0:
                
        str = str[:n] + str[n + 1:]

    return str
