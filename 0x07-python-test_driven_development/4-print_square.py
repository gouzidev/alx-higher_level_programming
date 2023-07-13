#!/usr/bin/python3
"""
    print
    square
    with size
"""


def print_square(size):
    """
    prints size of square
    Args:
        size: size lol
    """
    if type(size) not in [int, float]:
        raise TypeError("size must be an integer")

    if size < 0:
        if type(size) == int:
            raise ValueError("size must be >= 0")
        if type(size) == float:
            raise TypeError("size must be an integer")
    i = 0
    while (i < size):
        print("#" * size)
        i = i + 1
