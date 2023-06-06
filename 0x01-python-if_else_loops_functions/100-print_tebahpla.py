#!/usr/bin/python3
for i in range(122, 96, -1):
    x = (i % 2 == 0)
    print("{}".format(chr(i) if x else chr(i).upper()), end="", sep="")
