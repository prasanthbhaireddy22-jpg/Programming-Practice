# dictionary methods help to perform operations on dictionaries

# program 1
# using keys(), values(), items()

student = {
    "name": "Prasanth",
    "age": 18,
    "course": "Python"
}

print("Student Dictionary:", student)

print("\nKeys:")
print(student.keys())

print("\nValues:")
print(student.values())

print("\nItems:")
print(student.items())


# program 2
# using get() method

marks = {
    "math": 85,
    "science": 90,
    "english": 88
}

subject = input("\nEnter subject name to get marks: ")

print("Marks:", marks.get(subject, "Subject not found"))


# program 3
# using update() and pop()

student = {
    "name": "Ravi",
    "age": 19,
    "city": "Delhi"
}

print("\nOriginal Dictionary:", student)

# updating dictionary
student.update({"age": 20, "course": "Python"})

print("After Update:", student)

# removing a key
removed_value = student.pop("city")

print("Removed Value:", removed_value)
print("Final Dictionary:", student)