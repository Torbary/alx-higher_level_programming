#!/usr/bin/python3
"""
The module '1-my_list' 
"""


class MyList(list):
    """ subclass of a list"""
    def __init__(self):
        """Instantiate the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))

