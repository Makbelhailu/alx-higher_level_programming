#!/usr/bin/python3
"""class with personal info"""


class Student:
    """manage studentes info"""

    def __init__(self, first_name, last_name, age):
        """run first when class called"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return the dictionary"""
        dicts = {}
        if type(attrs) is list and all([type(attr) == str for attr in attrs]):
            for i in attrs:
                dicts[i] = self.__dict__[i]

            return dicts
        else:
            return self.__dict__
