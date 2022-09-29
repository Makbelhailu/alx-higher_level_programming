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
        if type(attrs) is list and all([type(attr) == str for attr in attrs]):
            return {key: val for key, val in self.__dict__.items() if key in
                    attrs}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """reload json from given argument"""
        for key, val in json.items():
            self.__dict__[key] = val
