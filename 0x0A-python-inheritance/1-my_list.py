#!/usr/bin/python3
""" list in order """

class MyList(list):
    """MyList class""" 
    
    def print_sorted(self):
        """prints list in ascending order"""
        sorted = self.copy()
        sorted.sort()
        print(sorted)
