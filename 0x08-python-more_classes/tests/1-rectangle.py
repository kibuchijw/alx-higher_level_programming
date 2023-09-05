#!/usr/bin/python3
""" Class Rectangle implementation, with private attributes"""


class Rectangle:
    """ Defines rectangle with private attributes width and height """

    def __init__(self, width=0, height=0):
        """
        Initializes new Rectangle object

        Args:
            width(int): The width, defaulting to 0
            height(int): The height, defaulting to 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for the rectangle width

        Returns:
            int: Width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the rectangle width

        Args:
            Value (int): Value of new width

        Raises:
            TypeError: if provided value is not an integer
            ValueError: if provided value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the rectangle height

        Returns:
            int: Height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the rectangle height

        Args:
            value (int): New height value

        Raises:
            TypeError: If provided value is not an integer
            ValueError: If provided value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
