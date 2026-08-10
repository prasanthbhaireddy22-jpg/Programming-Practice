# string formatting is used to insert values into a string

# program 1
# student details using format()

name = input("Enter student name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")

message = "Student Name: {}\nAge: {}\nCourse: {}".format(name, age, course)

print("\nStudent Details")
print(message)


# program 2
# bill generation using f-string

product_name = input("\nEnter product name: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total_amount = price * quantity

print(f"\nProduct Name: {product_name}")
print(f"Price: {price}")
print(f"Quantity: {quantity}")
print(f"Total Amount: {total_amount}")


# program 3
# marks report using formatting

student_name = input("\nEnter student name: ")

math = int(input("Enter math marks: "))
science = int(input("Enter science marks: "))
english = int(input("Enter english marks: "))

total = math + science + english
average = total / 3

report = f"""
Student Report
--------------
Name: {student_name}
Math: {math}
Science: {science}
English: {english}
Total: {total}
Average: {average}
"""

print(report)
