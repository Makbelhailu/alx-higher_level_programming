#!/usr/bin/python3
"""module for add_integer method
   Args:
       a: the first int
       b: the second int, by default its value is 98
"""


def add_integer(a, b=98):
    """Adds two integers of a and b,
    Return: The sum of a and b.
    """

    if (type(a) is not int) and (type(a) is not float):
        raise TypeError("a must be an integer")
    if (type(b) is not int) and (type(b) is not float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
