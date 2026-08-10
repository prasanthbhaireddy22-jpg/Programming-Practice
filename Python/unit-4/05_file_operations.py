# file handling is used to store data permanently

# program 1
# writing to a file

file = open("sample.txt", "w")

file.write("Hello, this is my first file\n")
file.write("Learning Python file handling\n")
file.write("This is very useful in real projects")

file.close()

print("File written successfully")


# program 2
# reading a file

file = open("sample.txt", "r")

print("\nFile Content:\n")

content = file.read()
print(content)

file.close()


# program 3
# reading file line by line

file = open("sample.txt", "r")

print("\nReading line by line:\n")

for line in file:
    print(line.strip())

file.close()