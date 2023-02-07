#!/usr/bin/python3
"""module '9-rectangle' """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


Rectangle = __import__('8-rectangle').Rectangle


class Rectangle(BaseGeometry):
    """subclass representing a rectangle"""
    def __init__(self, width, height):
        """ intstantiate rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """retrun the informal repr of sttring"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
