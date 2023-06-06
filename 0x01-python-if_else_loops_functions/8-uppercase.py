#!/usr/bin/python3
def uppercase(str):
    for c in str:
        cond = ord(c) > 96 and ord(c) < 123
        print(f"{chr(ord(c) - 32) if cond else c}", sep="", end="")
    print()
