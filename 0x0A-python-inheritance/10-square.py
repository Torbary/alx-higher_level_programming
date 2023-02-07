#!/usr/bin/python3
"""module '10-square'
    contains the class Bae Gemetry and sublass Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """subclass representing a square"""
    def __init__(self, size):
        """instantiate the class Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __area(self):
        """returns the area of a square"""
        return (self.__size ** 2)
