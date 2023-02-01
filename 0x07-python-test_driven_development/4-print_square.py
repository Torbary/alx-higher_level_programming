#!/usr/bin/python3
""" This is 4-print_square module that takes one function print_sqaure"""


def print_square(size):
    """This function prints a sqaure with the char #"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
        
    
