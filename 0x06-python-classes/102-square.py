#!/usr/bin/python3
"""define a classd sqaure"""


class Square:
    """Represent a square
    Attributes:
        __size (int): size of a side of a square
    """
    def __init__(self, size=0):
        """Iinitialize the square
        Args:
            size (int): size of a side of a square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """calculates the area of a sqaure
        Returns:
            The area of a square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of  __size
        Returns:
            The size of a square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): the size of a size of d sqaure
        Returns:
            NOne
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def __lt__(self, other):
        """COmpare if square is less than another by area
        Args:
            other (sqaure): sqaure to compare against
        Returns:
            True of False
        """
        return self.size < other.size

    def __le__(self, other):
        """compare if sqaure is less than or equal to another square
        Args:
            Other (sqaure): sqaure to compare against
        Returns:
            True or False
        """
        return self.size <= other.size

    def __eq__(self, other):
        """Compare if square is eqaual to another by area
        Args:
            Other (square): sqaure to compare against
        Returns:
            True or False
        """
        return self.size == other.size

    def __ne__(self, other):
        """Compare if square is not equal to another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size != other.size

    def __ge__(self, other):
        """Compare if square is greater than or equal to another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size >= other.size

    def __gt__(self, other):
        """Compare if square is greater than another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size > other.size
