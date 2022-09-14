#!/usr/bin/python3
"""Class with square"""


class Square:
    """Square  size and area"""

    def __init__(self, size=0):
        """Class size"""
        if type(size) is not int:
            raise TypeError("size must be a number")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def __lt__(self, other):
        """Compare with <"""
        return (self.area() < other.area())

    def __gt__(self, other):
        """Compare with >"""
        return (self.area() > other.area())

    def __le__(self, other):
        """Compare with <="""
        return (self.area() <= other.area())

    def __ge__(self, other):
        """Compare with >="""
        return (self.area() >= other.area())

    def __eq__(self, other):
        """Compare with =="""
        return (self.area() == other.area())

    def __ne__(self, other):
        """Compare with !="""
        return (self.area() != other.area())

    def area(self):
        """Return area"""
        return (self.__size ** 2)

    @property
    def size(self):
        """Getter for size"""
        return (self.__size ** 2)

    @size.setter
    def size(self, value):
        """Setter for size"""
        if (type(value) is not int) or (type(value) is not float):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be a number")
