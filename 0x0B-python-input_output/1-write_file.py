#!/usr/bin/python3
"""
Write string to a text file and return number of characters written
param filename: name of file to write to. param text: str to write
return: Number of characters written to file
"""


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file UTF8
    """

    with open(filename, "w", encoding="utf-8") as file:
        num_chars_written = file.write(text)
    return num_chars_written
