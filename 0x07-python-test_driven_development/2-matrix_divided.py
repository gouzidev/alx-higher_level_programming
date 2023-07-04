#!/usr/bin/python3
"""
    matrix division module
"""


def matrix_divided(matrix, div):
    """ Takes a matrix and divides the values by 'div'.

    Args:
        matrix (:obj:'list' of :obj:'list'): lists of lists of integers/floats.
        div (int or float): The divisor.
    """
    row_length = -1
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list or len(matrix) is 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/"
                        "floats")

    new = []
    for i in matrix:
        if type(i) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")
        if row_length is -1:
            row_length = len(i)
            if row_length is 0:
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")
        else:
            if row_length is not len(i):
                raise TypeError("Each i of the matrix must have the same "
                                "size")
        new_row = []
        for j in i:
            if type(j) is int or type(j) is float:
                new_row.append(round(j / div, 2))
            else:
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")
        new.append(new_row)
    return new
