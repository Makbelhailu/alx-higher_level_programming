#!/usr/bin/python3
"""module of Rectangle class"""


class Rectangle:
    """Class of rectangle"""
    number_of_instances = 0
    """int: number_of_instance"""

    print_symbol = "#"
    """any type: symbol for printing rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return area"""
        return self.__width * self.__height

    def perimeter(self):
        """return perimeter of rectangle"""
        if (self.__width == 0) or (self.__height == 0):
            return 0
        else:
            return 2 * (self.__width + self.height)

    def __str__(self):
        """print the area"""
        if not self.width or not self.height:
            return ""
        else:
            return ((str(self.print_symbol) * self.__width + '\n') *
                    self.__height)[:-1]

    def __repr__(self):
        """Returns formal string representation..."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Called when deleting an instance of rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest of the two rectangles.
        Args:
            rect_1: The first rectangle.
            rect_2: The second rectangle.
        Raises:
            TypeError: If rect_1, rect_2 are not instances of Rectangle.
        Return:
            The rectangle with the larger area.
        """
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """create new class"""
        return cls(size, size)
