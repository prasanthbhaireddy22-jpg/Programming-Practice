# input validation is used to make sure the user enters valid data

# program 1
# validate age input

age = int(input("Enter your age: "))

while age < 0 or age > 120:
    print("Invalid age. Please enter a valid age.")
    age = int(input("Enter your age again: "))

print("Your valid age is:", age)


# program 2
# validate marks input

marks = int(input("\nEnter your marks (0 to 100): "))

while marks < 0 or marks > 100:
    print("Invalid marks. Marks should be between 0 and 100.")
    marks = int(input("Enter marks again: "))

print("Valid marks entered:", marks)


# program 3
# validate password length

password = input("\nCreate a password (minimum 6 characters): ")

while len(password) < 6:
    print("Password is too short")
    password = input("Enter password again: ")

print("Password created successfully")