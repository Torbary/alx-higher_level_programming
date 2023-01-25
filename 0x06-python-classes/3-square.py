#!/usr/bin/python3
"""a class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """instantiate class"""
    def __init__(self, size=0):
        """ check if size != int"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            """check if size is less than 0"""
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """return the square of the area of sqaure"""
        return self.__size**2
