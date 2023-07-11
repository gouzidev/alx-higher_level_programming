#!/usr/bin/python3
"""
    Module containing add_integer function.
    The function returns two integers.
    5 line module comment.
"""
def add_integer(a, b=98):
    """ adds two integers 
    (or floats)
    and returns sum """
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    if type(a) != int or type(b) != int:
        raise TypeError("a must be an integer or b must be an integer")
    return a + b

