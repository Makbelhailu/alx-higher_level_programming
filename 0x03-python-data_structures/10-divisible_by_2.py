#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    a = len(my_list)
    new = my_list.copy()
    for i in range(a):
        if my_list[i] % 2 == 0:
            new[i] = True
        else:
            new[i] = False
    return (new)
