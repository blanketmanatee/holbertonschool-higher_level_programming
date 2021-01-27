#!/usr/bin/python3
""" base of all classes for this project """


class Base:
    """ class with private class attribute nb_objects """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
