#!/usr/bin/python3
"""Module 100-append_after.
Inserts a line of text to a file,
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """Appends the new_string after
    the search_string in filename.
    Args:
        - filename: name of  file
        - search_string: string to add after
        - new_string: new_string to add
    """

    with open(filename, "r") as f:
        content = f.readlines()

    with open(filename, "w") as fo:
        string = ""
        for l in content:
            string += l
            if search_string in l:
                string += new_string
        fo.write(string)
