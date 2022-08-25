#!/usr/bin/python3
if __name__ == "_main__":
    import sys

    agrs = len(sys.argv) - 1
    if args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op = sys.argv[2]
    if op != '+' or op != '-' or op != '*' or op !='/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    from calculator_1 import add, sub, mul, div
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if op == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    if op == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    if op == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    if op == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))