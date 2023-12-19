#!/usr/bin/python3

# -----------------------------------------------------------
# Python function that demonstrates how to print the numbers from 1 to 100 separated by a space
#
# (C) 2023, Silas Edet, Uyo, Nigeria
# email: silasedetsnr@gmail.com
# -----------------------------------------------------------

def fizzbuzz():
    
    for number in range(1, 101):

        if number % 3 == 0 and number % 5 != 0:

            print("Fizz ", end=" ")

        elif number % 5 == 0 and number % 3 != 0:

            print("Buzz ", end=" ")

        elif number % 3 == 0 and number % 5 == 0:

            print("FizzBuzz ", end=" ")

        else:
            print("{:d} ".format(number), end=" ")
