#!/usr/bin/python3
"""append the content into file"""


def append_write(filename="", text=""):
    """function that append"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
