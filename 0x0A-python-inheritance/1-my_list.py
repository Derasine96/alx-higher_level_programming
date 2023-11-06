#!/usr/bin/python3
"""a class that inherits from a list"""


class MyList(list):
    """a subclass of list"""
    def __init__(self):
        """Initialize a MyList by inheriting from list

        Args:
            args (list): List of numbers to initialize the MyList with
        """
        super().__init__()

    def print_sorted(self):
        """Prints a list of numbers in sorted order"""
        sorted_list = sorted(self)
        print(sorted_list)
