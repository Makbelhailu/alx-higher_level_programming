#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list = list(a_dictionary.keys())
    list.sort()
    for i in list:
        print("{}: {}".format(i, a_dictionary.get(i)))
