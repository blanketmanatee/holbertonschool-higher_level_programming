#!/usr/bin/python3
""" new class """


class BaseGeometry:
    """ public instance method def area(self):
    raises exception with message area() is not
    implemented """
    def area(self):
        raise Exception("area() is not implemented")
