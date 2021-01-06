#!/usr/bin/python3
"""class square defines a square and raises exceptions"""

class Square:
    """class square"""
    def __init__(self, size=0):
        """module"""
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
                raise TypeError('size must be an integer')
