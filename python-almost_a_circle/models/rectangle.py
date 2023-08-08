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

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
            y (int, optional): The y-coordinate of the rectangle's position.
            id (int, optional): The unique identifier of the rectangle.

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not greater than 0.

        """
        self.validate_value("width", value)
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not greater than 0.

        """
        self.validate_value("height", value)
        self.__height = value

    @property
    def x(self):
        """Get or set the x-coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle's position.

        Args:
            value (int): The new x-coordinate value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.

        """
        self.validate_value("x", value)
        self.__x = value

    @property
    def y(self):
        """Get or set the y-coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle's position.

        Args:
            value (int): The new y-coordinate value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.

        """
        self.validate_value("y", value)
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The calculated area.

        """
        return self.width * self.height

    def display(self):
        """Display the rectangle using '#' characters."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """Return a string representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args):
        """Update the Rectangle instance attributes.

        Args:
            *args: Variable-length arguments representing the new values for attributes.

        Returns:
            None

        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                if i == 0:
                    setattr(self, attrs[i], value)
                elif i < len(attrs):
                    setattr(self, attrs[i], value)
                else:
                    break





