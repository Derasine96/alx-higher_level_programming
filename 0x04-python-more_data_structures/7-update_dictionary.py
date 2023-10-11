#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary and a_dictionary[key] == value:
        return a_dictionary
    else:
        update = a_dictionary[key] = value
    return update
