#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        fct(args[0], args[1])
    except (NameError, ValueError, TypeError, ZeroDivisionError) as er:
        printf(f"Exception: {er}", file=sys.stderr)
        return None
