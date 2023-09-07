#!/usr/bin/python3
""" Class Rectangle implementation, with private attributes"""


class Rectangle:
    """ Defines rectangle with private attributes width and height """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes new Rectangle object

        Args:
            width(int): The width, defaulting to 0
            height(int): The height, defaulting to 0
        """
        Rectangle.number_of_instances += 1
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

    def area(self):
        """
        Calculate area of a rectangle

        Returns:
            int: Area of a rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate perimeter of a rectangle

        Returns:
            int: Perimeter of a rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        String representation of rectangle as pattern of '#'

        Returns:
            str: String representation of a rectangle
        """
        if self.width == 0 or self.height == 0:
            return ""

        rectangle_string = ""
        for _ in range(self.height):
            rectangle_string += str(self.print_symbol) * self.width + "\n"
        return rectangle_string[:-1]  # Remove trailing newline

    def __repr__(self):
        """
        Returns string representation of
        rectangle that can be used to recreate new instance

        Returns:
            str: String representation of rectangle
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Deleted instance of rectangle and prints message

        Returns:
            None
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the bigger rectangle, based on area

        Args:
            rect_1: First rectangle
            rect_2: Second rectangle

        Raises:
            TypeError: If rect_1 or rect_2 aren't instances

        Returns:
            Rectangle: The bigger rectangle, based on area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Creates new rectangle with width == height == size

        Args:
            size (int, optional): Size of square

        Returns:
            Rectangle: New rectangle presenting square
        """

        return cls(size, size)
