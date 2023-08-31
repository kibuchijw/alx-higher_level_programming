#!/usr/bin/python3
""" Define class Square """


class Square:
    """
    This class represents a square

    Attributes:
        __size (int): Size of square(private).
    """
    def __init__(self, size=0):
        """
        Initializes square instance

        Args:
            size(int, optional): Size of the square, default 0

            Raises:
                TypeError: If size if not an integer
                ValueError: If size if less than 0
        """
        self.__size = size

    @property
    def size(self):
        """
        Get size of square

        Returns:
            int: Size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set size of square

        Args:
            value(int): New size of square

        Raises:
            TypeError: If value is not integer
            ValueError: If value if less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


    def area(self):
        """
        Computes and returns area of square

        Returns:
            int: Area of the square

        """
        return self.__size ** 2
