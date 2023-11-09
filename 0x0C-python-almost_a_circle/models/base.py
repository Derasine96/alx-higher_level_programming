#!/usr/bin/python3
"""Base class"""


class Base:
    """My first base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor

        Args:
            id (int): Integer to be assigned (optional)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
