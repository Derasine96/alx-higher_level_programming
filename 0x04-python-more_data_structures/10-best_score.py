#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_key = 0
    max_score = 0
    for key, value in a_dictionary.items():
        if max_score == 0 or value > max_score:
            max_key = key
            max_score = value
    return max_key
