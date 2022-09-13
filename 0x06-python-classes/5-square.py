#!/usr/bin/python3
"""
class with size
- calculate area
- print_square method
- getter and setter
"""


class Square:
    """create class size area and print it"""
    def __init__(self, size=0):
        """constractor of class size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns its area"""
        return (self.__size ** 2)

    def my_print(self):
        """print the area with # form"""
        if self.__size == 0:
            print()
        else:
            for row in range(self.__size):
                print("#" * self.__size)

    @property
    def size(self):
        """getter for retriving size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter for setting size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
