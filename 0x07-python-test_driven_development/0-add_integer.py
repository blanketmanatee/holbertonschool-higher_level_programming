#!/usr/bin/python3
""" Addition """


def add_integer(a, b):
    """ 
    A and B must be ints or floats
    otherwise TypeError raise. 
    A and B must be casted if they are floats.
    Returns an int.
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (a + b)
    