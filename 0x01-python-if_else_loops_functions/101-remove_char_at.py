#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    new = ""
    for ch in str:
        if i != n:
            new += ch
        i += 1
    return new
