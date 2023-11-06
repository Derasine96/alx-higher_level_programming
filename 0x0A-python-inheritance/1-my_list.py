#!/usr/bin/python3
"""a class that inherits from a list"""


class MyList(list):
    def __init__(self, *args):
        """Initialize a MyList by inheriting from list

        Args:
            args (list): List of numbers to initialize the MyList with
        """
        if not all(isinstance(num, int) for num in args):
            raise TypeError("All elements of the list must be integers")
        super().__init__(args)

    def print_sorted(self):
        """Prints a list of numbers in sorted order"""
        sorted_list = sorted(self)
        print(sorted_list)
