#!/usr/bin/python3

"""
    this module does some calculations
    maybe
    5 lines
"""


def add_integer(a, b=98):
    """ Adds two numbers
    Args:
        a : the first
        b : the second
    """
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = float(b)
    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")
    return a + b
