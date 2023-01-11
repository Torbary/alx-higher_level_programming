#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    c_set = [value for value in set_1 ^ set_2]
    return c_set
