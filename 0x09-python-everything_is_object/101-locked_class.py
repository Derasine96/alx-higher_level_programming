#!/usr/bin/python3
"""Define a locked class with exception"""


class LockedClass:
    """Represents a lockedclass"""
    __slots__ = ['first_name']

    def __init__(self, first_name=None):
        """Initializes a instance

        Args:
            first_name(string): The new attribute
        """
        self.first_name = first_name
