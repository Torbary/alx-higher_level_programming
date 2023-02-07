#!/usr/bin/python3
"""
    Modules that contain 11-square module,
    subclass Square inherits from Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


Rectangle = __import__('9-rectangle').Rectangle


Square = __import__('10-square').Square


class Square(Rectangle):
    """subclass inherited from Rectangle"""
    def __init__(self, size):
        """instantiate the class Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """retrun area of a square"""
        return (self.__size ** 2)

    def __str__(self):
        """return the informal representation of a string"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
