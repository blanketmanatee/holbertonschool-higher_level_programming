#!/usr/bin/python3
""" adds all arguments to a python list then save to file """

import json
from sys import argv

save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

try:
    list = load('add_item.json')
except:
    list = []
list.extend(argv[1:])
save(list, "add_item.json")
