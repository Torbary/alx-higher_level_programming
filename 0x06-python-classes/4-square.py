#!/usr/bin/python3
"""a class Square that defines a square by: (based on 3-square.py)"""


class Square:
    """Represent a square
    Attributes:
         __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """INitialize the sqaure
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """calculate the area of square
        Returns:
            The area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """gettter of __size
        Returns:
            The size of the sqaure
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            Value (int): the size of a size of tghe square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
