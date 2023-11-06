#!/usr/bin/python3
"""Define a Base Geometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a Rectangle Subclass"""

    def __init__(self, width, height):
        """Creates an instance of width and height

        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
