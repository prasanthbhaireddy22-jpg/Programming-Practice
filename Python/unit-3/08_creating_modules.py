# a module is just a python file with functions inside it

# program 1
# creating simple functions in same file (module concept)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("\nAddition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))


# program 2
# function to check prime number

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

number = int(input("\nEnter a number: "))

if is_prime(number):
    print(number, "is Prime")
else:
    print(number, "is Not Prime")


# program 3
# function for simple interest calculation

def simple_interest(p, t, r):
    return (p * t * r) / 100

p = float(input("\nEnter principal: "))
t = float(input("Enter time: "))
r = float(input("Enter rate: "))

print("Simple Interest:", simple_interest(p, t, r))