#!/usr/bin/python3
"""mix all tasks"""
import json
from sys import argv

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filenane =  "add_item.json"


try:
    json_list = load_from_json_file(file_name)
except:
    json_list = []
    for i in argv[1:]:
        json_list.append(i)

    save_to_json_file(json_list, filename)
