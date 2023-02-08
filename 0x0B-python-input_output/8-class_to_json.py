#!/usr/bin/python3
"""
    contains the function class_to_json(obj)
"""


def class_to_json(obj):
    """
        function that returns thr dict descripition
        with simple data structure JSON serialization
        of an object:
    """
    return obj.__dict__


