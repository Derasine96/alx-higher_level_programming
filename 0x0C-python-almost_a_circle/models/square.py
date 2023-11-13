#!/usr/bin/python3
"""Defines a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square is a rectangle with equal sides."""

    def __init__(self, size, x=0, y=0, id=None):
        """The square class constructor

        Args:
            size (int): value of width and height(since it's a square)
            x : x coordinate Defaults to 0.
            y : y coordinate Defaults to 0.
            id: Defaults to None.
        """
        super().__init__(size, size, x, y, id=id)

    def area(self):
        """Return the current area of the square."""
        return self.width * self.width

    def __str__(self):
        """Return the str() representation of a Rectangle."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for the width of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the widthe of the square."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
        if args:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) in {2, 3, 4}:
                ar = [self.id, self.width, self.x, self.y]
                for i in range(min(len(args), 4)):
                    ar[i] = args[i]
                self.id, self.width, self.x, self.y = ar

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        square_dict = {}
        square_dict['id'] = self.id
        square_dict['size'] = self.width
        square_dict['x'] = self.x
        square_dict['y'] = self.y
        return square_dict
