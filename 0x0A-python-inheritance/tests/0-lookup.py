#!/usr/bin/python3
""" Looks up the list of available attributes and methods of an object """


def lookup(obj):
    attributes_and_methods = dir(obj)

    return attributes_and_methods
