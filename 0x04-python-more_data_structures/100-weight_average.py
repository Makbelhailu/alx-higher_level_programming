#!/usr/bin/python3
def weight_average(my_list=[]):
    a = len(my_list)
    num = 0
    div = 0

    if a == 0:
        return 0

    for i in range(a):
        for j in range(len(my_list[i])):
            num += my_list[i][j]
        div += my_list[i][1]
    new = num / div
    return (new)
