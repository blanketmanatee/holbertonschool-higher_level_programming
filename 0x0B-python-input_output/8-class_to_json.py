#!/usr/bin/python3
""" returns dict description w simple data structure for json serialization """


def class_to_json(obj):
    """ returns dict description """
    return obj.__dict__
