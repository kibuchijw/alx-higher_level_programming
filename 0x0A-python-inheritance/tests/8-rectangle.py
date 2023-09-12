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

class Rectangle(BaseGeometry):
    """
    Inherits from BaseGeometry
    """
    def __init__(self, width, height):
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
