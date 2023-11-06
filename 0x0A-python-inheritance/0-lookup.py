#!/usr/bin/python3
"""Returns list of available methods"""


def lookup(obj):
    """Returns a list

    Arg:
        obj(object): object to be listed
    """
    return dir(obj)
