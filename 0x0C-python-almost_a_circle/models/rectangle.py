#!/usr/bin/python3
"""Defines a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """A rectangle that inherits from Base with attributes."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """The rectangle class constructor

        Args:
            width: width of the rectangle
            height: height of the rectangle
            x : x coordinate Defaults to 0.
            y : y coordinate Defaults to 0.
            id: Defaults to None.
        """
        super().__init__(id=id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the current width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the current height of new rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the current x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the current y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the current area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Prints in stdout the Rectangle instance"""
        print('\n' * self.y, end="")
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
        if args:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) in {2, 3, 4}:
                ar = [self.id, self.width, self.height, self.x, self.y]
                for i in range(min(len(args), 5)):
                    ar[i] = args[i]
                self.id, self.width, self.height, self.x, self.y = ar

    def __str__(self):
        """Return the str() representation of a Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        rect_dict = {}
        rect_dict['id'] = self.id
        rect_dict['width'] = self.width
        rect_dict['height'] = self.height
        rect_dict['x'] = self.x
        rect_dict['y'] = self.y
        return rect_dict

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        dummy_object = cls(1, 1)
        dummy_object.update(**dictionary)
        return dummy_object
