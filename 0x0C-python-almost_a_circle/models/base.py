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

    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): List of dictionaries.
        """
        import json

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
        import json

        filename = cls.__name__ + ".json"

        if list_objs is None:
            with open(filename, 'w') as fp:
                fp.write('[]')
        else:
            with open(filename, 'w') as fp:
                fp.write(cls.to_json_string(list_objs))

    @classmethod
    def to_json_string(cls, list_objs):
        """Converts a list of instances to a JSON string.

        Args:
            list_objs (list): List of instances.
        """
        def custom_encoder(obj):
            """Custom encoder function for instances of Rectangle."""
            if isinstance(obj, cls):
                return obj.to_dictionary()
            return obj
        if list_objs is None:
            return "[]"
        else:
            return json.dumps(list_objs, default=custom_encoder)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string

        Args:
            json_string (str): JSON string rep.
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)
