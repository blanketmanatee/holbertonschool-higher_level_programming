#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry):
    """ inherits from BaseGeometry
    instantation with width and height
    def: __init__(self, width, height):
    width and height must be private w no
    getter or setter, also must be positive
    and validated by integer_validator
    print() should print and str() should return
    [Rectangle] <width>/<height> """

     self.integer_validator("width", width)
     self.integer_validator("height", height)
     self.__width = width
     self.__height = height

     def area(self):
         """returns area"""
         return self.__width * self.__height

     def __str__(self)
     """ return description of rectangle """
     return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
