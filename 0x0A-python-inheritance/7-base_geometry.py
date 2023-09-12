#!/usr/bin/python3
"""
Class based off of 5-base_geometry.py
Has a public instance method
Raises: Exception, with the message "Area not implemented"
"""


class BaseGeometry:
    """
    Public instance method
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Integer validator
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
