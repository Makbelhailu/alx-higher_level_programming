#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    if leng == 0:
        new = (leng, None)
    else:
        first = sentence[0]
        new = leng, first
    return (new)
