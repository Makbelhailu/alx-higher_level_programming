#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    leng = len(my_list)
    if idx < 0 or idx > leng:
        return (my_list)
    for i in range(leng):
        if i == idx:
            my_list[i] = []
    return (my_list)
