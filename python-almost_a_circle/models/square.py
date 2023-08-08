#!/usr/bin/python3

"""
This is the 'square' module.

This module contains the Square class which inherits from the Rectangle class
and represents a square with equal width and height attributes.

"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    The Square class, a subclass of Rectangle.

    Attributes:
        size (int): The size of the square.
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.
        id (int): The unique identifier of the square.

    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's position.
            y (int, optional): The y-coordinate of the square's position.
            id (int, optional): The unique identifier of the square.

        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

def display(self):
    """Display the square using '#' characters."""
    for _ in range(self.y):
        print()
    for _ in range(self.size):
        print(" " * self.x, end="")
        print("#" * self.size)
