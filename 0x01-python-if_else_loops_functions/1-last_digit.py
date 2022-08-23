#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    num = (-number % 10) * -1
elif number > 0 or number == 0:
    num = number % 10
message = f"Last digit of {number} is"
if num > 5:
    print(message, num, "and is greater than 5")
elif num < 6 and number % 10 != 0:
    print(message, num, "and is less than 6 and not 0")
else:
    print(message, num, "and is 0")
