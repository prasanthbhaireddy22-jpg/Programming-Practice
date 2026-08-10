# if-elif-else is used when there are multiple conditions

# program 1
# grading system

student_name = input("Enter student name: ")
marks = int(input("Enter marks: "))

print("\nStudent Grade Report")

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
elif marks >= 35:
    grade = "D"
else:
    grade = "Fail"

print("Name:", student_name)
print("Marks:", marks)
print("Grade:", grade)


# program 2
# traffic signal system

signal = input("\nEnter traffic signal color (red/yellow/green): ")

if signal == "red":
    print("Stop the vehicle")
elif signal == "yellow":
    print("Get ready")
elif signal == "green":
    print("Go")
else:
    print("Invalid signal")


# program 3
# electricity bill calculator

units = int(input("\nEnter electricity units used: "))

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = units * 3
elif units <= 300:
    bill = units * 4
else:
    bill = units * 5

print("\nElectricity Bill Details")
print("Units Consumed:", units)
print("Total Bill Amount:", bill)