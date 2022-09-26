#!/usr/bin/python3
"""
A class with inherited class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A subclass of BaseGeometry"""

    def __init__(self, width, height):
        """validate the height and width"""
        super().integer_validator("height", height)
        super().integer_validator("width", width)
        self.__width = width
        self.__height = height
        
    def area(self):
        """return the area"""
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
