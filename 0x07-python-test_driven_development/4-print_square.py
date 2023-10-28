#!/usr/bin/python3
"""
Define a function that prints a square with the character #.
This module can be imported and used to print # in a matrix format
The size must be included: length of the square
"""


def print_square(size):
    """Prints # in a matrix format

    Args:
        size (int): size length of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(0, size):
        if size == 0:
            print('')
        else:
            for col in range(0, size):
                print('#', end='')
        print('')
