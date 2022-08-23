#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    num = number * -1
else:
    num = number
message = f"Last digit of {number} is"
if num % 10 > 5:
    print(message, num % 10, "and is greater than 5")
elif num % 10 < 6 and number % 10 != 0:
    print(message, num % 10, "and is less than 6 and not 0")
else:
    print(message, num % 10, "and is 0")
