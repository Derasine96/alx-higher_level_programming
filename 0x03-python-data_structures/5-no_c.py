#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for string in my_string:
        if string != 'c' and string != 'C':
            result += string
    return result
