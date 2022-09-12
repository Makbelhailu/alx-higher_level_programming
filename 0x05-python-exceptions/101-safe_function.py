#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except Exception as er:
        print(f"Exception: {er}", file=sys.stderr)
        return None
    else:
        return res
