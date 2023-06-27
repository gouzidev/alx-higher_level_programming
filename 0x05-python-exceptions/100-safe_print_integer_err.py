#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    res = False
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        sys.stderr.write("Exception: Unknown format code\
                          '{}' for object of type 'str'\n".format(value))
        return False
