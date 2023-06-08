#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    somme = 0
    for arg in argv[1:]:
        somme += int(arg)
    print(somme)
