#!/usr/bin/python3

# [1, 2]
# last = 2 - 1
# last [1] -> 2

# [9]
# last = 1 - 1
# last [0] -> 9


def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    for i in range(length - 1, -1, -1):
        print("{:d}".format(my_list[i]))