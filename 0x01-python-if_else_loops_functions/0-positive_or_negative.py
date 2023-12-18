#!/usr/bin/python3

# -----------------------------------------------------------
# Python program that demonstrates how to determine if a number stored in a variable is positive or negative
#
# (C) 2023, Silas Edet, Uyo, Nigeria
# email: silasedetsnr@gmail.com
# -----------------------------------------------------------

import random
number = random.randint(-10, 10)

if number > 0:
    print("{} is positive".format(number))

elif number == 0:
    print("{} is zero".format(number))

else:
    print("{} is negative".format(number))
