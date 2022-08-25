#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 0
    result = 0
    for arg in sys.argv:
        if i != 0:
            result += int(arg)
        i += 1
    print(result)
