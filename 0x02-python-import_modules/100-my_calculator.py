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
        res = add(a, b)
    elif op == "-":
        res = sub(a, b)
    elif op == "/":
        res = div(a, b)
    elif op == "*":
        res = mul(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, op, b, res))
    exit(0)
