#!/usr/bin/python3
"""
Defines an integer addition function

This module can be imported and used to perform basic addition operations
with numeric values, whether they are integers or floats.
"""


def add_integer(a, b=98):
    """
    Add two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float, optional): The second number. Defaults to 98.

    Returns:
    int: The sum of the two numbers.

    Raises:
    TypeError: If either `a` or `b` is not an integer or a float.
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
