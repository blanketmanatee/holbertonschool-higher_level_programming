#!/usr/bin/python3
""" Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class square inherits class Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        "initialize the instance"
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ squares """
        s = "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.size)
        return s

    @property
    def size(self):
        """ finds size """
        return self.__width
    
    @size.setter
    def size(self, value):
        """ validates size """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    
