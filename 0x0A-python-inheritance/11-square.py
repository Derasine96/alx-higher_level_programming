#!/usr/bin/python3
"""Define a Base Geometry."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a Square Subclass"""

    def __init__(self, size):
        """Creates an instance of width and height

        Args:
            size(int): size of thed square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return f"[{self.__class__.__name__}] {self.__size}/{self.__size}"
