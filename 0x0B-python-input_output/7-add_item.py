#!/usr/bin/python3
"""
A script that passes objects to add a JSON object
If file is present, add items
If not present, create a new one
"""
import json
import os
import sys


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text file, using JSON
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """
    Function that creates an Object from a JSON file
    """

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


if os.path.exists("add_item.json"):
    my_list = load_from_json_file("add_item.json")
else:
    my_list = []

#  Add command-line arguments to list
for arg in sys.argv[1:]:
    my_list.append(arg)

#  Save updated list to file
save_to_json_file(my_list, "add_item.json")
