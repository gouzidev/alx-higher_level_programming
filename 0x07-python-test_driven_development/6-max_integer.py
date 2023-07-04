#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    res = list[0]
    idx = 1
    while idx < len(list):
        if list[idx] > res:
            res = list[idx]
        idx += 1
    return res
