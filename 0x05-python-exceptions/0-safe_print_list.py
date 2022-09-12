#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    y = 0
    while True:
        try:
            for i in range(x):
                print(my_list[i], end="")
                y += 1
            print("")
            break
        except IndexError:
            print("")
            break
    return (y)
