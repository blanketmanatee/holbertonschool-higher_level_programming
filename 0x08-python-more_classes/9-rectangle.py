#!/usr/bin/python3
"""Class rectangle"""


class Rectangle:
    """ rectangle class """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """size"""
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def height(self):
        """finding height"""
        return self.__height

    @height.setter
    def height(self, value):
        """validates height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """finding width"""
        return self.__width

    @width.setter
    def width(self, value):
        """validates width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """calculates area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calculates perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """ returns printed rectangle """
        shape = ""
        if self.__width == 0 or self.__height == 0:
            return shape
        for i in range(self.height):
            shape += str(self.print_symbol) * self.width
            if i < self.height - 1:
                shape += "\n"
        return shape

    def __repr__(self):
        """ rectangle representation """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ deleting instance """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1
    
    def square(cls, size=0):
        return cls(size, size)
