#!/usr/bin/python3
"""module for '8-rectangle.py'
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """subclass that inherit from BaseGeometry
       A representation of a retangle
    """
    def __init__(self, width, height):
        """instantiate Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
