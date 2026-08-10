# tuples are used to store multiple values
# tuples are immutable (cannot be changed)

# program 1
# creating and accessing tuple elements

student = ("Prasanth", 18, "Python")

print("Student Details")
print("Name:", student[0])
print("Age:", student[1])
print("Course:", student[2])


# program 2
# finding length and counting elements

numbers = (10, 20, 30, 20, 40, 20)

print("\nTuple:", numbers)
print("Length of tuple:", len(numbers))
print("Count of 20:", numbers.count(20))
print("Index of 30:", numbers.index(30))


# program 3
# checking item in tuple

fruits = ("apple", "banana", "mango", "orange")

fruit_name = input("\nEnter fruit name to search: ")

if fruit_name in fruits:
    print(fruit_name, "is available in tuple")
else:
    print(fruit_name, "is not available")

print("All fruits in tuple:")

for fruit in fruits:
    print(fruit)