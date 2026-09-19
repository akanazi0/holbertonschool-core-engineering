#!/usr/bin/env python3
number = __import__('random').randint(-10000, 10000)
if number < 0:
    last_digit = -(-number % 10)
else:
    last_digit = number % 10
print(f"Last digit of {number} is {last_digit}")
