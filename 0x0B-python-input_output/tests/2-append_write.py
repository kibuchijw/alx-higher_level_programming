#!/usr/bin/python3
"""
Append string to a text file and return number of characters written
param filename: name of file to append to. param text: str to append
return: Number of characters appended to file
"""


def append_write(filename="", text=""):
    """
    Function that appends a string to a text file UTF8
    """

    with open(filename, "a", encoding="utf-8") as file:
        num_chars_appended = file.write(text)
    return num_chars_appended
