#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Extracting the last digit of the number using modulus operator
last_digit = abs(number) % 10

# Checking conditions for the last digit
if last_digit > 5:
    print("The string Last digit of", number, "is", last_digit, "and is greater than 5")
elif last_digit == 0:
    print("The string Last digit of", number, "is", last_digit, "and is 0")
else:
    print("The string Last digit of", number, "is", last_digit, "and is less than 6 and not 0")
