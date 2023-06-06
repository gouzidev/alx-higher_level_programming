#!/usr/bin/python3
for i in range(10):
    for j in range(i, 10):
        if i != j:
            print("{}{}".format(i, j), sep="", end="")
        if j != 9 and i != 9 and j != 0:
            print(", ", sep="", end="")
print()
