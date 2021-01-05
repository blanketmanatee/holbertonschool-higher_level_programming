#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    printer = 0

    for x in range(x):
        try:
            if not isinstance(my_list[x], int):
                raise ValueError
            print("{:d}".format(my_list[x]), end='')
            printer = printer + 1
        except ValueError:
            pass
    print("")
    return printer
