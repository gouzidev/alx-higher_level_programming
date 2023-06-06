#!/usr/bin/python3
for i in range(100):
    if i != 99:
        print(f"{i:02d}, ", end="", sep=" ")
    else:
        print("{}".format(i).zfill(2))