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
            print(line.strip(), end="")
            print("\n", end="")
            print("\n", end="")
            line = ""
    if line:
        line = line.strip()
        if line != "":
            print(line)