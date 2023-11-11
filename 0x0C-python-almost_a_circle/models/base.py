#!/usr/bin/python3
"""Base class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): List of dictionaries.
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps([obj.to_dictionary() for obj in list_dictionaries])

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): List of instances.
        """
        filename = cls.__name__ + ".json"

        if list_objs is None:
            with open(filename, 'w') as f:
                f.write('[]')
        else:
            with open(filename, 'w') as f:
                f.write(cls.to_json_string(list_objs))

    @classmethod
    def to_json_string(cls, list_objs):
        """Converts a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): List of dictionaries.
        """
        return json.dumps([obj.to_dictionary() for obj in list_objs])
