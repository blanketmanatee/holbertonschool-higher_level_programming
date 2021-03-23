#!/usr/bin/python3
""" writes a str"""


def write_file(filename="", text=""):
    """ writes a str to a txt file and returns
    number of characters written """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
