#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, div, mul, sub
    if (len(argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])
    if op == "+":
        res = a + b
        print("{} {} {} = {}".format(a, op, b, res))
    elif op == "-":
        res = a - b
        print("{} {} {} = {}".format(a, op, b, res))
    elif op == "/":
        res = a / b
        print("{} {} {} = {}".format(a, op, b, res))
    elif op == "*":
        res = a * b
        print("{} {} {} = {}".format(a, op, b, res))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
