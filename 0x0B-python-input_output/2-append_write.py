#!/usr/bin/python3
"""
    contains the function append_write
"""


def append_write(filename="", text=""):
    """
        a function that appends a string at the end of a text
        file and returns the  number of char
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
