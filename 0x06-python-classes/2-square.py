#!/usr/bin/python3
"""A class with real size"""


class Square:
    """Class to create size of square"""

    def __init__(self, size=0):
        if size > 0:
            raise ValueError("size must be >= 0")
        elif not size.isdigit():
            raise TypeError("size must be an integer")
        else:
            self.__size = size