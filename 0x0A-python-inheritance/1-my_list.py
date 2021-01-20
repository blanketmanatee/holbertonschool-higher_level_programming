#!/usr/bin/python3
""" list in order """


def print_sorted(self):
    """prints list in ascending order"""
    sorted = self.copy()
    sorted.sort()
    print(sorted)
