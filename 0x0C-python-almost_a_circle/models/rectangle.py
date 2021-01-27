#!/usr/bin/python3
""" Class Rectangle inherits from Base """
from models.base import Base


class Rectangle(Base):
    """ class Rectangle inherits base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize instance """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ finding width """
        return self.__width

    @width.setter
    def width(self, value):
        """ validating width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ finding height """
        return self.__height

    @height.setter
    def height(self, value):
        """ validating height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ finding x """
        return self.__x

    @x.setter
    def x(self, value):
        """ validating x """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ finding y """
        return self.__y

    @y.setter
    def y(self, value):
        """ validating y """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area """
        return self.width * self.height

    def display(self):
        """ printing the shape """
        if self.width == 0 or self.height == 0:
            print("")
            return
        for h in range(0, self.height):
            [print('#', end="") for w in range(self.width)]
            print("")
        if self.x == 0 or self.y == 0:
            print("")
            return
        for x in range(0, self.x):
            [print('#', end="") for x in range(self.x)]
            print("")

    def __str__(self):
        """ describing the shape """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format
        (self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ adding args and kwargs """
        if len(args) != 0:
            i = 0
            attr = ['id', 'width', 'height', 'x', 'y']
            for arg in args:
                setattr(self, attr[i], args[i])
                i += 1
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)
