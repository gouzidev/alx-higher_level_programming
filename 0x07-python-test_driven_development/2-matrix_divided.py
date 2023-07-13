#!/usr/bin/python3

"""
    matrix devided
    a function that divides
    all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    matrix devided
    Args:
        matrix: a matrix
        div: a div value
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if matrix == []:
        raise TypeError(error)
    new_matrix = []
    size = len(matrix[0])
    for my_list in matrix:
        if my_list == []:
            raise TypeError(error)
        curr_list = []
        size_counter = 0
        for element in my_list:
            if type(element) not in [int, float]:
                raise TypeError(error)
            size_counter += 1
            curr_list.append(round(element / div, 2))
        if size != size_counter:
            raise TypeError("Each row of the matrix must have the same size")
        new_matrix.append(curr_list)
    return new_matrix
