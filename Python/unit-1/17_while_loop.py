# while loop executes as long as the condition is true

# program 1
# print numbers from 1 to 10

number = 1

print("Numbers from 1 to 10")

while number <= 10:
    print(number)
    number += 1


# program 2
# sum of first n natural numbers

n = int(input("\nEnter a number: "))

count = 1
total = 0

while count <= n:
    total = total + count
    count += 1

print("Sum of first", n, "numbers is:", total)


# program 3
# password checking system

correct_password = "python123"
entered_password = ""

while entered_password != correct_password:
    entered_password = input("\nEnter password: ")

    if entered_password != correct_password:
        print("Wrong password, try again")

print("Login Successful")