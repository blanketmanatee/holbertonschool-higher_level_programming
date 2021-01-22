#!/usr/bin/python3
""" inheritance """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ inherits from BaseGeometry
    instantation with width and height
    def: __init__(self, width, height):
    width and height must be private w no
    getter or setter, also must be positive
    and validated by integer_validator
    print() should print and str() should return
    [Rectangle] <width>/<height> """
     
def __init__(self, width, height):
     super().integer_validator("width", width)
     self.__width = width
     super().integer_validator("height", height)
     self.__height = height

     def __str__(self):
          """ return description of rectangle """
          return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

     def area(self):
          """returns area"""
          return self.__width * self.__height
