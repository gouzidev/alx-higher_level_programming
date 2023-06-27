#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    res = False
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        sys.stderr.write("Exception: Unknown format code\
                          '{}' for object of type '{}'\n".format(e.args[0], e.args[1]))
        return False
