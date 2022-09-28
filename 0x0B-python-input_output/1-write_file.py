#!/usr/bin/python3
"""write contents in file"""


def write_file(filename="", text=""):
    """the function that write"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
