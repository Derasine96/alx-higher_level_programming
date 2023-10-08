#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    add_a = tuple_a[0] if len(tuple_a) >= 1 else 0
    add_b = tuple_a[1] if len(tuple_a) >= 2 else 0
    add_a += tuple_b[0] if len(tuple_b) >= 1 else 0
    add_b += tuple_b[1] if len(tuple_b) >= 2 else 0
    return (add_a, add_b)
