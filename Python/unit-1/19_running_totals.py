# running total means adding values continuously in a loop

# program 1
# total marks of student

student_name = input("Enter student name: ")

total_marks = 0

for i in range(1, 6):
    mark = int(input("Enter mark " + str(i) + ": "))
    total_marks = total_marks + mark

print("\nStudent Name:", student_name)
print("Total Marks:", total_marks)


# program 2
# sum of expenses

days = int(input("\nEnter number of days: "))

total_expense = 0

for i in range(1, days + 1):
    expense = float(input("Enter expense for day " + str(i) + ": "))
    total_expense = total_expense + expense

print("\nTotal Expense:", total_expense)


# program 3
# adding even numbers from 1 to n

n = int(input("\nEnter a number: "))

total_even = 0

for number in range(1, n + 1):
    if number % 2 == 0:
        total_even = total_even + number

print("Sum of even numbers:", total_even)