#!/usr/bin/python3
""" Class Rectangle inherits from Base """
from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None): 
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError ("width must be an integer")
        if value <= 0:
            raise ValueError ("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError ("height must be an integer")
        if value <= 0:
            raise ValueError ("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x
        
    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        if self.width == 0 or self.height == 0:
            print("")
            return
        for h in range(self.height):
            [print('#', end="") for w in range(self.width)]
            print("")
        if self.x == 0 or self.y == 0:
            print("")
            return
        for x in range(self.x):
            [print('#', end="") for x in range(self.x)]
            print("")

    def __str__(self):
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        if len(args) != 0:
            i = 0
            attr = ['id', 'width', 'height', 'x', 'y']
            for arg in args:
                setattr(self, attr[i], args[i])
                i += 1
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

