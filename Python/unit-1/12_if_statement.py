# if statement is used to check a condition
# if the condition is true, the block of code will execute

# program 1
# checking voting eligibility

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(name, "you are eligible to vote")


# program 2
# checking student pass or fail

student_name = input("Enter student name: ")
marks = int(input("Enter your marks: "))

if marks >= 35:
    print("Student Name:", student_name)
    print("Marks:", marks)
    print("Result: Pass")


# program 3
# checking bonus eligibility for employee

employee_name = input("Enter employee name: ")
salary = float(input("Enter salary: "))
years_of_service = int(input("Enter years of service: "))

if years_of_service >= 5:
    bonus = salary * 0.10

    print("\nEmployee Details")
    print("Name:", employee_name)
    print("Salary:", salary)
    print("Years of Service:", years_of_service)
    print("Bonus Amount:", bonus)