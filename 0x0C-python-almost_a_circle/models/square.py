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
        s = "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x, self.y, self.size)
        return s