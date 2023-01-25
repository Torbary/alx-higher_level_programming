#!/usr/bin/python3
"""define a sqaure by:{based on 0-square.py}"""


class Square:
    """Represent a square
    Attributes:
         __size (int): size of a side of the sqaure
    """
    def __init__(self, size):
        """Initialize a square
        Args:
            size (int): size of a side of a square
        Return: None
        """
        self.__size = size
