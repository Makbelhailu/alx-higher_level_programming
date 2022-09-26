#!/usr/bin/python3
"""A class with subclass list and print sorted list"""


class MyList(list):
    """return sorted of normal list"""

    def print_sorted(self):
        """print sorted list"""
        new = sorted(self)
        print(new)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
