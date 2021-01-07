#!/usr/bin/python3
""" class square gets area getter and setter """


class Square:
    """ class square """

    def __init__(self, size=0, position=(0, 0)):
        """ size and words """

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ finding size """
        return self.__size

    @size.setter
    def size(self, value):
        """ validates size """

        if type(value) is int:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value
        else:
                raise TypeError('size must be an integer')

    def area(self):
        """ area and words """
        return self.__size ** 2

    @property
    def position(self):
        """ position is here """

        return self.__position

    @position.setter
    def position(self, value):
        """ setting my position """

        if type(position) != tuple or len(value != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(position[0], int) is False or position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(position[1], int) is False or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """prints square with #"""
        if self.__size == 0:
            print()
            return
        for x in range(self.__size):
            print("#" * self.__size)
        return
