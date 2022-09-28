#!/usr/bin/python3
"""Module for a script that adds all arguments to a Python list"""
import json
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


filename = "add_item.json"


try:
    json_list = load_from_json_file(file_name)
except Exception:
    json_list = []
for i in argv[1:]:
    json_list.append(i)

save_to_json_file(json_list, filename)
