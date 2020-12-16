#!/usr/bin/python3

def no_c(my_string):
    if my_string:
        new_str = ''
        for i in my_string:
            if i == 'C' and i == 'c':
                return new_str
    return my_string
