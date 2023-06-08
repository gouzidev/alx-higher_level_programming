#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv) > 1
    if len(argv) == 2:
        a = "argument"
    else:
        a = "arguments"
    b = ":" if args else "."
    print("{} {}{}".format(len(argv) - 1, a, b))
    if args:
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
