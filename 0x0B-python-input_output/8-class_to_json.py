#!/usr/bin/python3
"""change class to json"""


def class_to_json(obj):
    """search for class dictionary and return it"""
    if hasattr(obj, "__dict__"):
        return obj.__dict__
    return {}
