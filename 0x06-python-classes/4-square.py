#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Represents a square"""
    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size

    @property
    def size(self):
        """Retrieve the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """set a Square.

        Args:
            value (int): The value of the new square.
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Returns current square area"""
        return self.__size * self.__size
