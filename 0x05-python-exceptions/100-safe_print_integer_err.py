#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    res = False
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        sys.stderr.write("{}\n".format(e.__str__()))
        return False
