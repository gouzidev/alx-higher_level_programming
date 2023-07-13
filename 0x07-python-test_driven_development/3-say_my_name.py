#!/usr/bin/python3
""" cool
    stuff
    lol
"""


def say_my_name(first_name, last_name=""):
    """
    this is cool
    Args:
        first_name : first name
        last_name : last name
    """
    if type(first_name) != str:
        raise Exception("first_name must be a string")
    if type(last_name) != str:
        raise Exception("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
