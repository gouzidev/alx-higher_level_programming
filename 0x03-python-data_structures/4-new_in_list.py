#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    copy = my_list[:]
    if idx >= 0 and idx < length:
        copy[idx] = element
    return copy
