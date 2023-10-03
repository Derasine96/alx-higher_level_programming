#!/usr/bin/python3
for i in range(122, 96, -1):
    print(''.join(chr(i).upper() if i % 2 != 0 else chr(i)), end='')
