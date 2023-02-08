#!/usr/bin/python3
"""contain '0-read_file' module
    function that reads an entire file
"""


def read_file(filename=""):
    """ function that read a text file"""
    with open("my_file_0.txt", encoding="utf-8") as f:
        for line in f:
            print(line, end='')
