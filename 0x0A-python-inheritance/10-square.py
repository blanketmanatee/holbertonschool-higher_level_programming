#!/usr/bin/python3
""" inheritance """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from rectangle
    instantiation w size: def __init__(self, size)
    size private w no getter or setter
    size must be positive int validated by integer_validator
    area() must by implemented. """

    def __init__(self, size):
        """initialize"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns the area """
        return self.__size ** 2
