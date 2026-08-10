# dictionaries store data in key-value pairs

# program 1
# creating a simple dictionary

student = {
    "name": "Ravi",
    "age": 18,
    "course": "Python"
}

print("Student Dictionary:", student)


# program 2
# accessing and updating dictionary values

student = {
    "name": "Sita",
    "marks": 85
}

print("\nOriginal Student Data:", student)

student["marks"] = 90   # updating value
student["city"] = "Hyderabad"  # adding new key

print("Updated Student Data:", student)


# program 3
# user input dictionary

student = {}

student["name"] = input("\nEnter name: ")
student["age"] = int(input("Enter age: "))
student["course"] = input("Enter course: ")

print("\nFinal Student Details:")
print(student)

print("\nKeys in dictionary:")
for key in student:
    print(key)

print("\nValues in dictionary:")
for value in student.values():
    print(value)