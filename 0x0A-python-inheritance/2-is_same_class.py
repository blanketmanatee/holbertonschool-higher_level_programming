#!/usr/bin/python3
""" checks using type """


def is_same_class(obj, a_class):
    """returns True if object is exactly
    and instance of specified class. if not
    return False. """
    return type(obj) is a_class
