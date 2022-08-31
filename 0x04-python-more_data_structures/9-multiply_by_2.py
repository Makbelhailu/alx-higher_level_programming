#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    lists = list(a_dictionary.keys())
    for i in lists:
        new[i] *= 2
    return (new)
