# keyword arguments allow passing values using parameter names

# program 1
# basic keyword arguments

def student(name, age, course):
    print("\nStudent Details")
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

student(age=18, course="Python", name="Prasanth")


# program 2
# mixing positional and keyword arguments

def add(a, b, c):
    print("\nValues:", a, b, c)
    print("Sum:", a + b + c)

add(10, c=30, b=20)


# program 3
# real-life bill system using keyword arguments

def bill(customer_name, item, price, quantity):
    total = price * quantity

    print("\n--- BILL RECEIPT ---")
    print("Customer Name:", customer_name)
    print("Item:", item)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Total Amount:", total)

bill(customer_name="Ravi", item="Book", price=50, quantity=4)