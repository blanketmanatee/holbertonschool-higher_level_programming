#!/usr/bin/python3
""" creates an object from a json file """
import json

def load_from_json_file(filename):
    """ create an object from json file """
    with open(filename, 'r', encoding="utf-8") as newfile:
        return json.load(newfile)
