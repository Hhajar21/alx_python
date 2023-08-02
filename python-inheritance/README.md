Python Inheritance Project
Python Badge

Overview
This project explores the concept of inheritance in Python. Inheritance is a powerful feature of object-oriented programming (OOP) that allows a class (subclass) to inherit properties and behaviors from another class (superclass). In this project, we will work on several tasks to understand and implement inheritance in Python.

Learning Objectives
After completing this project, you will be able to:

Explain why Python programming is awesome.
Understand the concepts of superclass, base class, and parent class.
Define and use subclasses in Python.
List all attributes and methods of a class or instance.
Implement inheritance in Python.
Define a class with multiple base classes.
Understand the default class every class inherits from.
Override methods or attributes inherited from the base class.
Access attributes or methods available by heritage to subclasses.
Understand the purpose of inheritance in Python.
Use isinstance, issubclass, type, and super built-in functions.
Requirements
Python Scripts
All code files should be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3 or later.
Code files should follow the PEP 8 style (version 1.7.*).
Each code file should end with a new line.
Documentation
A README.md file, at the root of the project folder, is mandatory.
Tasks
Exact Same Object

Write a function is_same_class(obj, a_class) that returns True if the object obj is exactly an instance of the specified class a_class; otherwise, it returns False.
Same Class or Inherit From

Write a function is_kind_of_class(obj, a_class) that returns True if the object obj is an instance of, or if the object is an instance of a class that inherited from, the specified class a_class; otherwise, it returns False.
Only Sub Class Of

Write a function inherits_from(obj, a_class) that returns True if the object obj is an instance of a class that inherited (directly or indirectly) from the specified class a_class; otherwise, it returns False.
Geometry Module

Write an empty class BaseGeometry.
Improve Geometry

Write a class BaseGeometry that has a public instance method area(self) that raises an Exception with the message "area() is not implemented".
Integer Validator

Write a class BaseGeometry that has a public instance method integer_validator(self, name, value) to validate the value:
The name parameter is always a string.
If value is not an integer, raise a TypeError exception with the message "<name> must be an integer".
If value is less than or equal to 0, raise a ValueError exception with the message "<name> must be greater than 0".
Rectangle

Write a class Rectangle that inherits from BaseGeometry. The Rectangle class has an instantiation with width and height as private attributes.
The __init__(self, width, height) method initializes the Rectangle object with positive integer values for width and height.
The width and height attributes must be validated using the integer_validator method from the BaseGeometry class.
Full Rectangle

Write a class Rectangle that inherits from BaseGeometry and overrides the __str__ method to return the following rectangle description: "[Rectangle] <width>/<height>".
The __str__ method should also implement the print() function to print the rectangle description.
Square #1

Write a class Square that inherits from Rectangle. The Square class has an instantiation with size as a private attribute.
The __init__(self, size) method initializes the Square object with a positive integer value for size.
The size attribute must be validated using the integer_validator method from the BaseGeometry class.
Conclusion
By completing this project, you will gain a solid understanding of inheritance in Python and its significance in object-oriented programming. You will be able to use and implement subclasses, override methods, and use inheritance to create more organized and reusable code. Happy coding!