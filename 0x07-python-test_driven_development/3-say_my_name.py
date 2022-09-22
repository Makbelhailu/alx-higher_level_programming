#!/usr/bin/python3
"""A function that print z name"""


def say_my_name(first_name, last_name=""):
    """print the full name
    Args:
        first_name
        last_name
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
