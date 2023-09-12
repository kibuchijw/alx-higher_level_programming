#!/usr/bin/python3
"""
Function that checks if object is exactly
an instance of specified class
Returns: A boolens, True or False
"""


def is_same_class(obj, a_class):
    """
    Checks if object is instance of class
    """
    return type(obj) is a_class
