#!/usr/bin/python3
"""
Read and print content of a text file(UTF-8) to stdout
param filename: Name of file to read
type filename: str
"""


def read_file(filename=""):
    """
    Reads and prints contents of a text file
    """

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
