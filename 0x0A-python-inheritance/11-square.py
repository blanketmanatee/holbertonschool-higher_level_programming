#!/usr/bin/python3
""" squares """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ based on previous task.
    print() should print and str() should
    return the square description """

    def __init__(self, size):
        """initialize"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

        def area(self):
            """returns the area """
            return super().area()

        def __str__(self):
            return "[Square] {}/{}".format(self.__size, self.__size)
