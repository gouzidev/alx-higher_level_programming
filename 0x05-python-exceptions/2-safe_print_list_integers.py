def safe_print_list_integers(my_list=[], x=0):
    i = 0
    n = 0
    while (i < x):
        try:
            print("{:d}".format(my_list[i]), end="", sep="")
        except (TypeError, ValueError):
            pass
        finally:
            n += 1
            i += 1
    print()
    return n