#!/usr/bin/python3
def max_integer(my_list=[]):
    leng = len(my_list)

    if leng == 0:
        return None
    maxlist = my_list[0]
    for i in range(1, leng):
        if maxlist < my_list[i]:
            maxlist = my_list[i]
    return (maxlist)
