#!/usr/bin/python3
def uppercase(str):
    for chars in str:
        if 'a' <= chars <= 'z':
            upper = chr(ord(chars) - ord('a') + ord('A'))
        else:
            upper = chars
        print('{}'.format(upper), end='')
    print()
