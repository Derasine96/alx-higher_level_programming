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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

