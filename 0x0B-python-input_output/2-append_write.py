#!/usr/bin/python3
""" appends a string at the end of text file """


def append_write(filename="", text=""):
    """ append a string """
    with open(filename, 'a', encoding="UTF-8") as newfile:
        return newfile.write(text)
