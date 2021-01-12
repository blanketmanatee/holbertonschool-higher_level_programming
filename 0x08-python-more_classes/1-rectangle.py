#!/usr/bin/python3
"""Class rectangle"""

class Rectangle:
    def __init__(self, width=0, height=0):
        """size"""

        self.__height = height
        self.__width = width

        @property
        def height(self):
            """finding height"""
            return self.__height

        @height.setter
        def height(self, value):
            """validates height"""

        @property
        def width(self):
            """finding width"""
            return self.__width

        @width.setter
        def width(self, value):
            """validates width"""

            if type(value) is int:
                if value < 0:
                    raise ValueError('width must be >= 0')
                else: self.__width = value

            else:
                raise TypeError('width must be an integer')
        