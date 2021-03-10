#!/usr/bin/python3
""" append after """

def append_after(filename="", search_string="", new_string=""):
    """ inserts lines """
    key = " "
    with open(filename, 'r', encoding='utf-8') as file:
        for i in file:
            key += i
            if search_string in i:
                key += new_string
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(key)
