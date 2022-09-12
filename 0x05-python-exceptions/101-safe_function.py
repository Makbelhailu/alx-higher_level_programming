#!/usr/bin/python3
from __future__ import print_function
import sys


def safe_function(fct, *args):
    try:
        res = fct(args[0], args[1])
    except Exception as er:
        print(f"Exception: {er}", file=sys.stderr)
        return None
    else:
        return res
