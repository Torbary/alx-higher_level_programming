#!/usr/bin/python3
"""
The module '2-is_same_class'
"""


def is_same_class(obj, a_class):
    """return the True if obj==instance"""
    return type(obj) is a_class
