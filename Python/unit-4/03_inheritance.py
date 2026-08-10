# inheritance means one class can use properties of another class

# program 1
# single inheritance

class Parent:
    def show_parent(self):
        print("This is Parent class")

class Child(Parent):
    def show_child(self):
        print("This is Child class")

c = Child()
c.show_parent()
c.show_child()


# program 2
# real-life example (student and result)

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_student(self):
        print("\nStudent Name:", self.name)
        print("Marks:", self.marks)

class Result(Student):
    def show_result(self):
        if self.marks >= 35:
            print("Result: Pass")
        else:
            print("Result: Fail")

s1 = Result("Ravi", 78)
s1.display_student()
s1.show_result()


# program 3
# multiple inheritance

class Father:
    def father_property(self):
        print("\nFather: Has land and house")

class Mother:
    def mother_property(self):
        print("Mother: Has savings")

class Child(Father, Mother):
    def child_property(self):
        print("Child: Uses both properties")

c1 = Child()
c1.father_property()
c1.mother_property()
c1.child_property()