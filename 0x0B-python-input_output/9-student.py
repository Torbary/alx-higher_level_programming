#!/usr/bin/python3
"""
    contain a class 'Student'
"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        """instantiate Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrive a dict rep of a Student"""
        return self.__dict__
