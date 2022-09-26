#!/usr/bin/python3
"""A class with method area"""


class BaseGeometry:
    """raise an exception"""

    def area(self):
        """exception raiser"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validet the int"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
