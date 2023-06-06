#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    s = ""
    while(i < len(str)):
        if i != n:
            s += str[i]
        i += 1
    return s
