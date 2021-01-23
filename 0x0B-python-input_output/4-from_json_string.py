#!/usr/bin/python3
""" returns an object from a str """
import json


def from_json_string(my_str):
    """ uses loads """
    return json.loads(my_str)
