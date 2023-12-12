#!/usr/bin/python3
# -----------------------------------------------------------
# Python function that computes the square value of all integers of a matrix using map
#
# (C) 2023, Silas Edet, Uyo, Nigeria
# email: silasedetsnr@gmail.com
# -----------------------------------------------------------

def square_matrix_map(matrix=[]):
    return list(map(lambda j: list(map(lambda i: i**2, j)), matrix))
