#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i < 2:
                result = result + (a / b) ** i
        except Exception:
            print('Too far')
        if i >= 3:
            break
        else:
            result = a + b
    return result
