#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, div, mul, sub
    if (len(argv) != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    a = int(argv(1))
    op = int(argv(2))
    b = int(argv(3))
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
