#!usr/bin/python3
"""class with square"""


class Square:
    """square - size - area"""

    def __init__(self, size=0):
        """class size"""
        if type(size) is not int:
            raise TypeError("size must be a number")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def __lt__(self, other):
        """compare with <"""
        return (self.area() < other.area())

    def __gt__(self, other):
        """ compare with >"""
        return (self.area() > other.area())

    def __le__(self, other):
        """compare with <="""
        return (self.area() <= other.area())

    def __ge__(self, other):
        """compare with >="""
        return (self.area() >= other.area())

    def __eq__(self, other):
        """compare with =="""
        return (self.area() == other.area())

    def __ne__(self, other):
        """compare with !="""
        return (self.area() != other.area())

    def area(self):
        """return area"""
        return (self.__size ** 2)

    @property
    def size(self):
        """getter for size"""
        return (self.__size ** 2)

    @size.setter
    def size(self, value):
        """setter for size"""
        if (type(value) is not int) or (type(value) is not float):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be a number")