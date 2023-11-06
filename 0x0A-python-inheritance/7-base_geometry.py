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
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
