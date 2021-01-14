#!/usr/bin/python3
"""Class rectangle"""


class Rectangle:
    """ Rectangle class width and height """
    def __init__(self, width=0, height=0):
        """ size """

        self.width = width
        self.height = height

    @property
    def width(self):
        """finding width"""
        return self.__width

    @width.setter
    def width(self, value):
        """validates width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """finding height"""
        return self.__height

    @height.setter
    def height(self, value):
        """validates height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
