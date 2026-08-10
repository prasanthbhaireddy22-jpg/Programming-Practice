# default arguments give a default value to parameters

# program 1
# greeting with default name

def greet(name="User"):
    print("Hello", name, "Welcome!")

greet()
greet("Prasanth")


# program 2
# adding numbers with default value

def add(a, b=10):
    print("a =", a)
    print("b =", b)
    print("Sum =", a + b)

num = int(input("Enter a number: "))

add(num)
add(num, 20)


# program 3
# student details with default course

def student_info(name, course="Python"):
    print("\nStudent Name:", name)
    print("Course:", course)

n = input("\nEnter student name: ")
student_info(n)
student_info(n, "Java")