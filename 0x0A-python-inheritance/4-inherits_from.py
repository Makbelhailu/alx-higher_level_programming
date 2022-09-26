#!/usr/bin/python3
"""A function that return True when the object is inheritance"""


def inherits_from(obj, a_class):
    """Return True when issubclass is true"""

    return (issubclass(type(obj), a_class))
