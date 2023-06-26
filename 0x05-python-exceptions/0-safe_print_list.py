#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    n_printed = 0
    try:
        while (i < x):
            print(my_list[i], end='', sep='')
            n_printed += 1
            i += 1
    except:
        return n_printed
    finally:
        print()
        return n_printed
