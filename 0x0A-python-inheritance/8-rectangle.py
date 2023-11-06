#!/usr/bin/python3
"""Define a Base Geometry."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Raise an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a value

        Args:
            name (str): name (a string) for the value
            value (int): value to validate
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
class Rectangle:
    """Represents a Rectangle Subclass"""

    def __init__(self, width, height):
        """Creates an instance of width and height

        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

