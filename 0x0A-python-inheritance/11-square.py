#!/usr/bin/python3
"""class with inherited class"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A class calculating square"""

    def __init__(self, size):
        """validate the size by inheriting the class"""
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """return area"""
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
