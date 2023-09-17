#!/usr/bin/python3
"""
Return Python data structute (object) represented by a JSON string
:param my_str: JSON string to be converted to Python object
:return: Python data structure represented by JSON string
"""
import json


def from_json_string(my_str):
    """
    Function that returns an object(Python data structute) from JSON
    """

    return json.loads(my_str)
