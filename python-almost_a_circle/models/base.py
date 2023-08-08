#!/usr/bin/python3

"""
This is the 'base' module.

This module contains the Base class which serves as the base for all other
classes in the project. It manages the id attribute and avoids duplicating
code across classes.

"""

class Base:
    """
    The Base class for all other classes.

    Attributes:
        __nb_objects (int): A private class attribute to keep track of the
        number of objects created.
        id (int): A public instance attribute representing the object's ID.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new Base instance.

        Args:
            id (int): The ID for the instance. If None, it is automatically
            assigned based on the number of objects.

        Returns:
            None

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
