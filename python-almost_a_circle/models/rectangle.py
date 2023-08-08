#!/usr/bin/python3

"""
This is the 'rectangle' module.

This module contains the Rectangle class which inherits from the Base class
and represents a rectangle with width, height, x, and y attributes.

"""

from models.base import Base

class Rectangle(Base):
    """
    The Rectangle class, a subclass of Base.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle's position.
        y (int): The y-coordinate of the rectangle's position.
    """

    # ... (previous code)

    def display(self):
        """
        Print the Rectangle using '#' characters.

        Returns:
            None

        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    # ... (previous code)
