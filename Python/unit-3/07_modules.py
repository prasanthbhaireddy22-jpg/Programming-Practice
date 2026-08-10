# modules are pre-built code libraries in python

# program 1
# using math module

import math

num = int(input("Enter a number: "))

print("\nSquare root:", math.sqrt(num))
print("Factorial:", math.factorial(num))
print("Power (num^2):", math.pow(num, 2))


# program 2
# using random module

import random

print("\nGenerating random numbers between 1 and 100:")

for i in range(5):
    print(random.randint(1, 100))


# program 3
# using from-import method

from math import sqrt, ceil

value = float(input("\nEnter a decimal number: "))

print("Square root:", sqrt(value))
print("Rounded up value:", ceil(value))