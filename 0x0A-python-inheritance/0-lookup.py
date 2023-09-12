#!/usr/bin/python3
"""
The function looks up  attributes and methods
It returns a list of all available to the object
Usage: Pass object for which to retrieve attributes and methods
"""


def lookup(obj):
    """
    Looks up the list of available attributes and methods of an object
    """
    attributes_and_methods = dir(obj)

    return attributes_and_methods
