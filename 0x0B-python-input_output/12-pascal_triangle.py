#!/usr/bin/python3
"""Module 14-pascal_triangle.
Returns a list of lists of integers
representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """Returns the pascal triangle of n.
    Args:
        - n: size of the triangle (rows)
    Returns: a list of list of integers
    """

    if n <= 0:
        return []

    arr = [[0 for x in range(i + 1)] for i in range(n)]
    arr[0] = [1]

    for x in range(1, n):
        arr[x][0] = 1
        for y in range(1, x + 1):
            if y < len(arr[x - 1]):
                arr[x][y] = arr[x - 1][y - 1] + arr[x - 1][y]
            else:
                arr[x][y] = arr[x - 1][0]
    return arr
