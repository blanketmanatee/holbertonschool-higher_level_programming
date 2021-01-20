#!/usr/bin/python3


class BaseGeometry:
    """public instance method def area(self):
    raises exception with message area() is not
    implemented. public instance method def integer_validator(self,name,value)
    validates value. name is alway a str. if value is not an int
    raise TypeError value must be an integer. if value is <= 0
    raise ValueError value must be greater than 0. """
    def area(self):
        """defines area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value)
    """ name is a str. if value is not int raise exception. if value is <= 0
    raise exception. """
    if type(value) is not int:
        raise TypeError("{} must be an integer")
    if value <= 0:
        raise ValueError("{} must be greater than 0")
