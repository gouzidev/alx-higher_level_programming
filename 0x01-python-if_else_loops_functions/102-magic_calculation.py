#!/usr/bin/python3
def magic_calculation(a, b, c):
    if (a < b):
        return c
    if (c > b):
        return a + b
    c = a * b
    return c - b

print(magic_calculation(30, 10, 2))