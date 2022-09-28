#!/usr/bin/python3
"""convert to jason to str"""
import json


def from_json_string(my_str):
    """fonction to convert"""
    return json.loads(my_str)
