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

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps([obj.to_dictionary()
                              for obj in list_dictionaries])

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
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set

        Args:
            **dictionary (dict): Key/value pairs of attributes to init.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    def update(self, *args, **dictionary):
        """Update self's attributes using kwargs or args"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        for key in dictionary:
            setattr(self, key, dictionary[key])

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a JSON file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                data = f.read()
                list_dicts = cls.from_json_string(data)
                instances = [cls.create(**obj_dict) for obj_dict in list_dicts]
                return instances
        except FileNotFoundError:
            return []
