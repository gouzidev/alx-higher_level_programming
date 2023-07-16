#!/usr/bin/python3
"""
    Module containing text indentation function
"""


def text_indentation(text):
    """ Text indentation function

    Args:
        text (str): A string of text
    """


    if type(text) != str:
        raise TypeError("text must be a string")
    line = ""
    for i in range(len(text)):
        line += text[i]
        if text[i] in [".", "?", ":"]:
            print(line.strip())
            print("\n", end="")
            line = ""
    if line:
            print(line.strip())
            print("\n", end="")