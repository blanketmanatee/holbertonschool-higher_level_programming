#!/usr/bin/python3
"""class square that calculates area"""


class Square:
"""class square"""
    def __init__(self, size=0):
        """size"""
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
                raise TypeError('size must be an integer')

    def area(self):
        """area"""
        return self.__size **2
