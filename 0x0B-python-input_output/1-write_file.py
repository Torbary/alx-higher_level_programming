#!/usr/bin/python3
"""
    contains write_file function
"""


def write_file(filename="", text=""):
    """ function that writes a string to a file
        and returns the number of char written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
