#!/usr/bin/python3
"""define a class MagicClass"""
import math


class MagicClass:
    def __init__(self, radius):
        """This represnt a circle"""
        self.__radius = 0
        if type(radius) not in (int, float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate the area of circle"""
        return math.pi * (self.__radius ** 2)

    def circumference(self):
        """Cal the circumference of a circle"""
        return 2 * math.pi * (self.__radius)
