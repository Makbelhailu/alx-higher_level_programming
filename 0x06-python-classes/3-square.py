#!/usr/bin/python3
"""Class with size and its area"""


class Square:
    """Create size of a class and its area"""

    def __init__(self, size=0):
        """Constractor of size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """calculate its area"""
        return (self.size ** 2)
