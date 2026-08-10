# custom exception logic

# program 1
# voting system validation

class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter age: "))

    if age < 0:
        raise InvalidAgeError("Age cannot be negative")

    if age < 18:
        print("Not eligible to vote")
    else:
        print("Eligible to vote")

except InvalidAgeError as e:
    print("Custom Error:", e)


# program 2
# password validation

password = input("\nEnter password: ")

try:
    if len(password) < 6:
        raise Exception("Password too short")

    print("Password accepted")

except Exception as e:
    print("Error:", e)


# program 3
# balance check system

balance = 500

try:
    withdraw = int(input("\nEnter withdrawal amount: "))

    if withdraw > balance:
        raise Exception("Insufficient balance")

    balance -= withdraw
    print("Remaining balance:", balance)

except Exception as e:
    print("Transaction failed:", e)