#!/usr/bin/python3
"""
Defines a rectangle based on '1-rectangle.py'
"""


class Rectangle:
    """Defines a real triangle, handles area and perimeter"""
    def __init__(self, width=0, height=0):
        """Instantiate class"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """cal the area of a circle"""
        return (self.__width * self.__height)

    @property
    def height(self):
        """retrive height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height"""
        if not isinstance(value, int):
            raise TypeError("heigth must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
