#!/usr/bin/python3
"""Class with MagicClass"""
import math


class MagicClass:
    """Define MagicClass"""
    def __init__(self, radius=0):
        """Initalize Data"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Get area"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Get circumference"""
        return (2 * math.pi * self.__radius)
