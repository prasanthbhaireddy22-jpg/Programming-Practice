# modules are used to access built-in functions and tools

# program 1
# using math module

import math

number = int(input("Enter a number to find square root: "))

square_root = math.sqrt(number)

print("The square root of", number, "is", square_root)


# program 2
# finding factorial using math module

import math

num = int(input("Enter a number to find factorial: "))

factorial_value = math.factorial(num)

print("The factorial of", num, "is", factorial_value)


# program 3
# using random module

import random

print("Generating 5 random numbers between 1 and 50")

for i in range(5):
    random_number = random.randint(1, 50)
    print("Random Number", i + 1, ":", random_number)