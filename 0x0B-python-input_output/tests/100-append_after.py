#!/usr/bin/python3
"""
:param filename: Name of file to operate on
:param search_string: String to search for in each line
:param new_string: Line of text to insert after each occurrence
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert line of text after each line containing specific string
    """
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    with open(filename, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
