#!/usr/bin/python3
"""A class that inherit int"""


class MyInt(int):
    """the Main class"""

    def __eq__(self, value):
        return False
    def __ne__(self, value):
        return True
