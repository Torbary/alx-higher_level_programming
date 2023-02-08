#!/usr/bin/python3
"""
    contains a class "Student" that deifnes a student
    contains a public method "to_json"
"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        """instantiate Student"""
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        """retrieve a dict rep of Student"""
        if attrs is None:
            return self.__dict__
        else:
            d = {}
            for attr in attrs:
                if hasattr(self, attr):
                    d[attr] = getattr(self, attr)
            return d
