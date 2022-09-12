#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(args[0], args[1])
    except (IndexError, Exception, ZeroDivisionError) as er:
        print(f"Exception: {er}", file=sys.stderr)
        return None
