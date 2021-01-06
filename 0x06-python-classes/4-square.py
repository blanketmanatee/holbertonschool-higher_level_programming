#!/usr/bin/python3
"""introducing getter and setter"""


class Square:
    """class square"""
    def __init__(self, size=0):
        """size and words"""
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
                raise TypeError('size must be an integer')

    def area(self):
        """area and words"""
        return self.__size **2

    @property
    def size(self):
        """finding size"""
        return self.__size

    @size.setter
    def size(self, value):
        """validates size"""
