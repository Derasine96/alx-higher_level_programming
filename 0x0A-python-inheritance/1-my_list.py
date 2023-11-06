#!/usr/bin/python3
"""a class that inherits from a list"""


class MyList(list):
    def __init__(self, *args):
        """Initialize a MyList by inheriting from list

        Args:
            args (list): List of numbers to initialize the MyList with
        """
    def print_sorted(self):
        """Prints a list of numbers in sorted order"""
        if not all(isinstance(num, int) for num in self):
            raise TypeError("All elements of the list must be integers")
        copy = self[:]
        copy.sort()
        print(copy)
