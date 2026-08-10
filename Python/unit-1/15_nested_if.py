# nested if means using one if statement inside another if statement

# program 1
# checking eligibility for driving license

name = input("Enter your name: ")
age = int(input("Enter your age: "))
documents = input("Do you have ID proof? (yes/no): ")

if age >= 18:
    if documents.lower() == "yes":
        print("\nLicense Application Approved")
        print("Name:", name)
    else:
        print("\nID proof is required")
else:
    print("\nNot eligible for driving license")


# program 2
# checking login system

username = input("\nEnter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "1234":
        print("\nLogin Successful")
    else:
        print("\nWrong Password")
else:
    print("\nInvalid Username")


# program 3
# student scholarship eligibility

student_name = input("\nEnter student name: ")
marks = int(input("Enter marks: "))
income = int(input("Enter family income: "))

if marks >= 80:
    if income <= 200000:
        print("\nScholarship Approved")
        print("Student:", student_name)
    else:
        print("\nIncome limit exceeded")
else:
    print("\nMarks are not enough for scholarship")