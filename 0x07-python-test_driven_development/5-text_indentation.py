#!/usr/bin/python3
"""
    Module containing text indentation function
"""


def text_indentation(text):
    """ Text indentation function

    Args:
        text (str): A string of text
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    no_space_flag = 1
    size = 0
    text = text.strip()
    string = ""
    for x in text:
        if x is " " and no_space_flag  == 1:
            pass
        elif x is "." or x is "?" or x is ":":
            string += x + "\n\n"
            no_space_flag = 1
        else:
            string += x
            no_space_flag = 0
    print(string, end='')
