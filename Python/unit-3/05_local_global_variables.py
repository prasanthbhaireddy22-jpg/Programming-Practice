# local variables are defined inside a function
# global variables are defined outside and can be used anywhere

# program 1
# local variable example

def show():
    x = 10  # local variable
    print("Inside function:", x)

show()

# print(x)  # this will give error if uncommented


# program 2
# global variable example

y = 50  # global variable

def display():
    print("\nInside function (global variable):", y)

display()
print("Outside function:", y)


# program 3
# modifying global variable inside function

count = 0

def increment():
    global count
    count = count + 1
    print("\nInside function count:", count)

increment()
increment()
increment()

print("Final count outside function:", count)