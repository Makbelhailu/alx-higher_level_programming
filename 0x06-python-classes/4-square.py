#!/usr/bin/python3
"""class with square size and area"""


class Square:
    """Create a class with size and its area"""

    def __init__(self, size=0):
        """Constractor of square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """calculate its area"""
        return (self.__size ** 2)

    @property
    def size(self):
        """property for retriving its size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter for Constractor of square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
