#!/usr/bin/python3
"""This is a function that divides each element of a matrix"""


def matrix_divided(matrix, div):
    """ Returns a new matrix """

    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) of " +
                        "integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_matrix.append(len(row))
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]
    return new_matrix
