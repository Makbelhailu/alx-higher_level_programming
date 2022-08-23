#!/usr/bin/python3
def fizzbuzz():
    f = "Fizz"
    b = "Buzz"
    fb = "FizzBuzz"
    for i in range(0, 101):
        if i % 3 != 0 and i % 5 != 0:
            print("{:d}".format(i, end=""))
        elif i % 3 == 0:
            print("{:s}".format(f, end=""))
        elif i % 5 == 0:
            print("{:s}".format(b, end=""))
        elif i % 5 == 0 and i % 3 == 0:
            print("{:s}".format(fb, end=""))
        if i != 100:
            print("{}". format(end=""))
