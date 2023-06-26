#\!usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    l = []
    i = 0
    while (i < list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print('division by 0')
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        except (TypeError, ValueError):
            print("wrong type")
            res = 0
        finally:
            i += 1
            l.append(res)
    return l