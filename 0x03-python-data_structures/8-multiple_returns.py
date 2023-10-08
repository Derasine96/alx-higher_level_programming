#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_result = ()
    if len(sentence) == 0:
        tuple_result = 0, 'None'
    else:
        first_char = sentence[0]
        tuple_result = (len(sentence), first_char)
    return tuple_result
