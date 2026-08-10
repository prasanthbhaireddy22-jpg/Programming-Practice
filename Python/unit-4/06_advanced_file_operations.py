# advanced file operations include readline, readlines, append and seek

# program 1
# writing and appending data

file = open("data.txt", "w")
file.write("Line 1: Python is easy\n")
file.write("Line 2: File handling is important\n")
file.close()

file = open("data.txt", "a")
file.write("Line 3: This line is added later\n")
file.close()

print("File written and appended successfully")


# program 2
# using readlines()

file = open("data.txt", "r")

print("\nReading all lines using readlines:\n")

lines = file.readlines()

for line in lines:
    print(line.strip())

file.close()


# program 3
# using seek() and readline()

file = open("data.txt", "r")

print("\nReading first line:")
print(file.readline().strip())

file.seek(0)  # move cursor back to start

print("\nReading again from start:")
print(file.read())

file.close()