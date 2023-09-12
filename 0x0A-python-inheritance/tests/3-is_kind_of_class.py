#!/usr/bin/python3
"""
Checks whether the object is an instance of,
or if object is an instance of a class that inherited from specified class.
Returns: True of False
"""

def is_kind_of_class(obj, a_class):
    """
    Checks whether same class or inherited
    """
    return isinstance(obj, a_class)
