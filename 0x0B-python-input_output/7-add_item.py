#!/usr/bin/python3
"""Load, add and save to a json file"""
import json
import sys


def save_to_json_file(my_obj, filename):
    """Function to write Json data to a file

    Args:
        my_obj: object to be written
        filename: file to write into
    """
    with open(filename, "w") as json_file:
        json.dump(my_obj, json_file)


def load_from_json_file(filename):
    """A function that creates an Object from a “JSON file”

    Arg:
        filename: file to create
    """
    with open(filename, "r") as json_file:
        object_file = json.load(json_file)
    return object_file


if __name__ == "__main__":
    try:
        my_obj = load_from_json_file("add_item.json")
    except (FileNotFoundError, json.JSONDecodeError):
        my_obj = []
    for arg in sys.argv[1:]:
        my_obj.append(arg)
    save_to_json_file(my_obj, "add_item.json")
