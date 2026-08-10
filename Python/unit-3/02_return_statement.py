# return statement is used to send a value back from a function

# program 1
# returning sum of two numbers

def add(a, b):
    return a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = add(num1, num2)

print("Sum is:", result)


# program 2
# returning largest number

def find_largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

x = int(input("\nEnter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

largest = find_largest(x, y, z)

print("Largest number is:", largest)


# program 3
# returning square and cube

def calculate(num):
    square = num * num
    cube = num * num * num
    return square, cube

number = int(input("\nEnter a number: "))

sq, cu = calculate(number)

print("Square:", sq)
print("Cube:", cu)