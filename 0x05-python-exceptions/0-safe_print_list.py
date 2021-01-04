#!/bin/usr/python3


def safe_print_list(my_list=[], x=0):
    for x in my_list:
        print("{:d}".format(x), end='')
