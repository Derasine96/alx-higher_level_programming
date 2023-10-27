#!/usr/bin/python3
"""
A function that divides all elements of a matrix.
This module can be imported and used to perform division of a matrix,
whether they are integers or floats.
"""

def matrix_divided(matrix, div):
    """Divide elements of a matrix

    Args:
        matrix (list of lists): 2 x 3 matrix of integers or floats
        div (int or float): divisor

    Returns:
        list of lists: a new matrix with elements divided by the divisor
    """
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ValueError("Divisor cannot be zero")
    row_size = len(matrix[0])
    if not all(isinstance(row, list) and len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            if not (isinstance(num, int) or isinstance(num, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_row.append(round(num / div, 2))
        new_matrix.append(new_row)
    return new_matrix
