# constructor is automatically called when object is created
# class attributes are shared by all objects

# program 1
# constructor example

class Student:
    def __init__(self, name, age):
        print("Constructor called")
        self.name = name
        self.age = age

    def display(self):
        print("\nName:", self.name)
        print("Age:", self.age)

s1 = Student("Ravi", 19)
s1.display()


# program 2
# class attribute example

class School:
    school_name = "ABC High School"  # class attribute

    def __init__(self, student_name):
        self.student_name = student_name

    def show(self):
        print("\nSchool Name:", School.school_name)
        print("Student Name:", self.student_name)

s1 = School("Kiran")
s2 = School("Sita")

s1.show()
s2.show()


# program 3
# modifying class attribute

class Company:
    company_name = "Tech Solutions"

    def __init__(self, employee):
        self.employee = employee

    def show(self):
        print("\nCompany:", Company.company_name)
        print("Employee:", self.employee)

c1 = Company("Arjun")
c2 = Company("Deepa")

Company.company_name = "Global Tech"  # changing class attribute

c1.show()
c2.show()