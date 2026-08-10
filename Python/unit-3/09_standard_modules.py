# standard modules are built-in modules provided by python

# program 1
# using datetime module

import datetime

current_time = datetime.datetime.now()

print("Current Date and Time:", current_time)

print("Year:", current_time.year)
print("Month:", current_time.month)
print("Day:", current_time.day)


# program 2
# using math + random together

import math
import random

num = random.randint(1, 10)

print("\nRandom Number:", num)
print("Square root:", math.sqrt(num))


# program 3
# using time module

import time

print("\nStarting countdown:")

for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

print("Time's up!")