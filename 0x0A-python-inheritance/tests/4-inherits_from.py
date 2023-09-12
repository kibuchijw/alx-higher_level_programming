#!/usr/bin/python3
"""
Checks whether object is an instance of a class
inherited(directly or indirectly) from specified class
Returns: True or False
"""


def inherits_from(obj, a_class):
    """
    Check for inheritance and returns boolean
    """
    return issubclass(type(obj), a_class)
