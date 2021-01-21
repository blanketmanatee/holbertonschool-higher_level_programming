#!/usr/bin/python3
""" reads a txt file and prints to stdout """


def read_file(filename=""):
    """function to read and write a txt file to stdout """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
