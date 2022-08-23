#!/usr/bin/python3
def islower(c):
    for i in range(26):
        char = chr(i + ord("a"))
        if c == char:
            return True
    return False
