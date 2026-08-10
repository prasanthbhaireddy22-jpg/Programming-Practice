# lambda functions are small anonymous functions
# used for simple operations in one line

# program 1
# square of a number

square = lambda x: x * x

num = int(input("Enter a number: "))

print("Square is:", square(num))


# program 2
# sum of two numbers

add = lambda a, b: a + b

x = int(input("\nEnter first number: "))
y = int(input("Enter second number: "))

print("Sum is:", add(x, y))


# program 3
# checking even or odd using lambda

check_even = lambda n: "Even" if n % 2 == 0 else "Odd"

number = int(input("\nEnter a number: "))

print("Result:", check_even(number))