#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in row:
            formatted_element = "{:d}".format(element)
            end_character = ' ' if element != row[-1] else ""
            print(formatted_element, end=end_character)
        print()
