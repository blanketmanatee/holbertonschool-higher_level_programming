#!/usr/bin/python3
""" checks using isinstance """


def is_kind_of_class(obj, a_class):
    """returns True if obj is an instance of
    or if obj is an instance of a class that
    inherited from the specified class. If not return
    False. """

    return isinstance(obj, a_class)
