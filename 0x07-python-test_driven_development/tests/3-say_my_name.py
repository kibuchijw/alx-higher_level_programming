#!/usr/bin/python3
"""
Print full name with greeting
First name should always be passed
Throw an error if name isn't string
"""

def say_my_name(first_name, last_name=""):
    """
    Print first and last name
    """

    # Check if first_name and last_name are strings
    if not (isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if not (isinstance(last_name, str)):
        raise TypeError("last_name must be a string")

    # Print greeting
    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")
