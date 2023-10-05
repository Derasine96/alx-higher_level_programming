#!/usr/bin/python3
import magic_calculation_102
def magic_calculation(a, b):
    if a < b:
        result = a + b
        for i in range(4, 7):
            result = magic_calculation_102.add(result, i)
        return result
    return magic_calculation_102.sub(a, b)
