# if-else statement
# if condition is true, one block executes
# otherwise else block executes

# program 1
# even or odd number checker

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(number, "is an even number")
else:
    print(number, "is an odd number")


# program 2
# checking pass or fail with result details

student_name = input("\nEnter student name: ")
marks = int(input("Enter marks: "))

if marks >= 35:
    print("\nStudent Result")
    print("Name:", student_name)
    print("Marks:", marks)
    print("Status: Pass")
else:
    print("\nStudent Result")
    print("Name:", student_name)
    print("Marks:", marks)
    print("Status: Fail")


# program 3
# checking bank account minimum balance

account_holder = input("\nEnter account holder name: ")
balance = float(input("Enter account balance: "))

minimum_balance = 1000

if balance >= minimum_balance:
    print("\nTransaction Allowed")
    print("Account Holder:", account_holder)
    print("Available Balance:", balance)
else:
    shortage = minimum_balance - balance
    print("\nTransaction Denied")
    print("Account Holder:", account_holder)
    print("Need extra balance of:", shortage)