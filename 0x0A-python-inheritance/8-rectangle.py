#!/usr/bin/python3
"""
A class with method area
"""


class BaseGeometry:
    """raise an exception"""
    def area(self):
        """raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value to be an int grater than 0.
        Args:
            name (str): name of the value
            value (unknown): to be validated.
        Raises:
            TypeError: if value is not an int.
            ValueError: if value is <= 0.
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """A subclass of BaseGeometry"""
    def __init__(self, width, height):
        """validate the height and width"""
        self.__width = width
        self.__height = height
        super().integer_validator("height", self.__height)
        super().integer_validator("width", self.__width)
