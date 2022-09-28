#!/usr/bin/python3
"""function prints the file content"""


def read_file(filename=""):
    """printer func"""
    with open(filename, 'r', encoding="utf-8") as f:
        file = f.read()
        print(file, end="")
