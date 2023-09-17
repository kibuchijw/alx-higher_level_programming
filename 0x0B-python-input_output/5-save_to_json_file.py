#!/usr/bin/python3
"""
Write an object to a text file using JSON representation
:param my_obj: Object to be serialized to JSON and saved
:param filename: Name of file to save JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text file, using JSON
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
