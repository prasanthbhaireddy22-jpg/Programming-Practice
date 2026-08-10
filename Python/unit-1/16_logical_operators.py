# logical operators are used to combine conditions
# and, or, not

# program 1
# checking college admission eligibility

student_name = input("Enter student name: ")
marks = int(input("Enter marks: "))
age = int(input("Enter age: "))

if marks >= 75 and age >= 17:
    print("\nAdmission Eligible")
    print("Student Name:", student_name)
else:
    print("\nNot Eligible for Admission")


# program 2
# checking login access using OR operator

username = input("\nEnter username: ")
password = input("Enter password: ")

if username == "admin" or password == "admin123":
    print("\nAccess Granted")
else:
    print("\nAccess Denied")


# program 3
# checking shop opening status using NOT operator

shop_closed = input("\nIs the shop closed? (yes/no): ")

if not (shop_closed.lower() == "yes"):
    print("\nShop is Open")
else:
    print("\nShop is Closed")