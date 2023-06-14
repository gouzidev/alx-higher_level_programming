#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    returned = {}
    for key in a_dictionary:
        returned[key] = a_dictionary[key] * 2
    return (returned)
