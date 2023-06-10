#!/usr/bin/python3
def no_c(my_string):
    copy = ""
    for c in my_string:
        if c != 'C' and c != 'c':
            copy += c
    return copy
