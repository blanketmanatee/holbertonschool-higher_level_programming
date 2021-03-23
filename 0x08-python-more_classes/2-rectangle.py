#!/usr/bin/python3
"""Class rectangle"""


class Rectangle:
    """ rectangle class """
    def __init__(self, width=0, height=0):
        """size"""

        self.width = width
        self.height = height

    @property
    def height(self):
        """finding height"""
        return self.__height

    @height.setter
    def height(self, value):
        """validates height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """finding width"""
        return self.__width

    @width.setter
    def width(self, value):
        """validates width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """calculates area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calculates perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)
