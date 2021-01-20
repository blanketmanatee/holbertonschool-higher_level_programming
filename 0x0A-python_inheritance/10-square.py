#!/usr/bin/python3
rectangle = __import__('9-rectangle.py').rectangle


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
        super().__init__(self.__size, self.__size)

        def area(self):
            """returns the area """
            return super().area()
