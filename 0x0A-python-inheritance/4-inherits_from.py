#!/usr/bin/python3
"""A function that return True when the object is inheritance"""


def inherits_from(obj, a_class):
    """Return True when issubclass is true"""

    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
