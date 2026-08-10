# lists are used to store multiple values in a single variable

# program 1
# adding and removing items in a list

students = ["Ravi", "Kiran", "Sita"]

print("Original List:", students)

new_student = input("Enter new student name: ")
students.append(new_student)

print("After Adding:", students)

remove_student = input("Enter student name to remove: ")

if remove_student in students:
    students.remove(remove_student)
    print("After Removing:", students)
else:
    print("Student not found")


# program 2
# finding largest and smallest numbers

numbers = []

for i in range(5):
    num = int(input("Enter number " + str(i + 1) + ": "))
    numbers.append(num)

print("\nNumbers List:", numbers)
print("Largest Number:", max(numbers))
print("Smallest Number:", min(numbers))
print("Total Sum:", sum(numbers))


# program 3
# searching an item in the list

products = ["Laptop", "Mouse", "Keyboard", "Monitor"]

search_product = input("\nEnter product name to search: ")

if search_product in products:
    print(search_product, "is available in the list")
else:
    print(search_product, "is not available")
    