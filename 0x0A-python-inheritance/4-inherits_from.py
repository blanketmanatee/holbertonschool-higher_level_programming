#!/usr/bin/python3
""" using type and insinstance """


def inherits_from(obj, a_class):
    """returns True if obj is an instance of
    a class that inherits (directly or indirectly)
    from specified class. If not return False. """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
