#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = len(my_list)
    for i in reversed(range(a)):
        print("{:d}".format(my_list[i]))
