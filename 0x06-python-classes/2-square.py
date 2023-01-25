#!/usr/bin/python3
""" a class Square that defines a square by: (based on 1-square.py)"""


class Square:
    """define a class sqaure"""
    def __init__(self, size=0):
        """check if size != int"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
