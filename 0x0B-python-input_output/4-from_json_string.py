#!/usr/bin/python3
"""
    contains a function from_json_string(my_str)
"""

import json


def from_json_string(my_str):
    """
        returns an obj represented by JSON string
    """
    return json.loads(my_str)
