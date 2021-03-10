#!/usr/bin/python3
""" class student based on task 9 """


class Student():
    """ class student """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves dict """
        if attrs is None:
            return self.__dict__
        dict = {}
        for a in attrs:
            try:
                dict[a] = self.__dict__[a]
            except:
                pass
        return dict
