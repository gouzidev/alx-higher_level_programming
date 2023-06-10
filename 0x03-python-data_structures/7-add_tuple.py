#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tup = []
    if len(tuple_a) > 1:
        if len(tuple_b) > 1:
            tup.append(tuple_a[0] + tuple_b[0])
            tup.append(tuple_a[1] + tuple_b[1])
            return tuple(tup)
        else:
            if len(tuple_b) == 1:
                tup.append(tuple_a[0] + tuple_b[0])
                tup.append(tuple_a[1])
                return tuple(tup)
            else:
                tup.append(tuple_a[0])
                tup.append(tuple_a[1])
                return tuple(tup)

    if len(tuple_b) > 1:
        if len(tuple_a) > 1:
            tup.append(tuple_b[0] + tuple_a[0])
            tup.append(tuple_b[1] + tuple_a[1])
            return tuple(tup)
        else:
            if len(tuple_a) == 1:
                tup.append(tuple_b[0] + tuple_a[0])
                tup.append(tuple_b[1])
                return tuple(tup)
            else:
                tup.append(tuple_b[0])
                tup.append(tuple_b[1])
                return tuple(tup)