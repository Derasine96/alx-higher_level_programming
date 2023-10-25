#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
            position (tuple): The x and y axis
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The value of the new square size.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Get the positions"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position to a new value

        Args:
            value (tuple): The new position.
        """
        if (not isinstance(value, tuple) or len(value) != 2
                or not all(isinstance(num, int) for num in value) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns current square area"""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square to stdout"""
        if self.__size == 0:
            print('')
        else:
            for j in range(0, self.__position[1]):
                print("")
            for _ in range(self.__size):
                print((" " * self.__position[0]) + ("#" * self.__size))
