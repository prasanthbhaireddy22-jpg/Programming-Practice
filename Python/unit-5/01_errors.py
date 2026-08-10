# advanced exception handling examples

# program 1
# multiple exception handling

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))

    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Enter only numbers")


# program 2
# list error handling

try:
    nums = [10, 20, 30]
    index = int(input("\nEnter index (0-2): "))

    print("Value:", nums[index])

except IndexError:
    print("Error: Index out of range")

except ValueError:
    print("Error: Invalid input")


# program 3
# safe file handling

try:
    file = open("test.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found")

finally:
    print("Program execution completed")