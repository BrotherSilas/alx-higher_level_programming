#!/usr/bin/python3
# -----------------------------------------------------------
# Python function that computes the square value of all integers of a matrix
#
# (C) 2023, Silas Edet, Uyo, Nigeria
# email: silasedetsnr@gmail.com
# -----------------------------------------------------------


def square_matrix_simple(matrix=[]):
    new_matrix = [[x**2 for x in row] for row in matrix]
    return new_matrix
