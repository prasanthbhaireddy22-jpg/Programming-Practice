# functions are used to reuse code

# program 1
# simple function to greet user

def greet():
    name = input("Enter your name: ")
    print("Hello", name, "Welcome to Python")

greet()


# program 2
# function with parameters

def add(a, b):
    result = a + b
    print("Sum is:", result)

num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))

add(num1, num2)


# program 3
# function to check even or odd

def check_even_odd(num):
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

number = int(input("\nEnter a number: "))
check_even_odd(number)