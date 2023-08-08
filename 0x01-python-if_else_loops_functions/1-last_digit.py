#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
conversion = abs(number) % 10
sign = -1 if number < 0 else 1
last_digit = conversion * sign
message = "Last digit of"
if last_digit > 5:
    print(f"{message} {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"{message} {number} is {last_digit} and is 0")
else:
    print(f"{message} {number} is {last_digit} and is less than 6 and not 0")
