#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        tuple_sen = (None, len(sentence))
    else:
        first_char = sentence[0]
        tuple_result = (len(sentence), first_char)
    return tuple_result
