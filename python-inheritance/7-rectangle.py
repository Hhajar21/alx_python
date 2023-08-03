#!/usr/bin/python3
"""
This module checks if an object is the instance of a class
class Rectangle 

"""

class BaseGeometry:
     """Represent a rectangle using BaseGeometry."""
     def area(self):
        raise Exception("area() is not implemented")

     def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """Intialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
         """Return the area of the rectangle."""
         return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
