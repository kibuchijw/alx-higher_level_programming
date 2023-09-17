#!/usr/bin/python3
import json
"""
Return JSON representation of an object as a string
param my_obj: Object to be converted to JSON
Return: JSON representation of object as a string
"""


def to_json_string(my_obj):
    """
    Function that returns JSON representation of an object(string)
    """

    return json.dumps(my_obj)
