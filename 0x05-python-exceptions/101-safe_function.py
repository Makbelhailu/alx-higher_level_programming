#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(args[0], args[1])
    except (IndexError, ValueError, TypeError, ZeroDivisionError) as er:
        print(f"Exception: {er}", file=sys.stderr)
        return None
    except (SyntaxError, RuntimeError):
        print(f"Exception: {er}", file=sys.stderr)
        return None
