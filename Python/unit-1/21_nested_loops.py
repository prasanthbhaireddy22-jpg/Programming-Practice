# nested loops means using one loop inside another loop

# program 1
# star pattern

rows = int(input("Enter number of rows: "))

print("\nStar Pattern")

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()


# program 2
# multiplication table from 1 to 5

print("\nMultiplication Tables from 1 to 5")

for i in range(1, 6):
    print("\nTable of", i)

    for j in range(1, 11):
        print(i, "x", j, "=", i * j)


# program 3
# student marks table

students = int(input("\nEnter number of students: "))
subjects = int(input("Enter number of subjects: "))

for i in range(1, students + 1):
    print("\nStudent", i)

    total = 0

    for j in range(1, subjects + 1):
        mark = int(input("Enter marks for subject " + str(j) + ": "))
        total = total + mark

    print("Total Marks of Student", i, ":", total)