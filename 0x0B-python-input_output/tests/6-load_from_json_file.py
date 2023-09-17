#!/usr/bin/python3
"""
Create an Object from a JSON file
:param filename: Name of JSON file to read and convert to object
:return: Python object represented by JSON data in file
"""
import json


def load_from_json_file(filename):
    """
    Function that creates an Object from a JSON file
    """

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
