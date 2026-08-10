# class is a blueprint
# object is an instance of a class

# program 1
# basic class and object

class Student:
    def show(self):
        print("This is a student class")

s1 = Student()
s1.show()


# program 2
# storing and displaying data using class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("\nName:", self.name)
        print("Age:", self.age)

p1 = Person("Ravi", 20)
p1.display()


# program 3
# multiple objects

class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show(self):
        print("\nBrand:", self.brand)
        print("Price:", self.price)

c1 = Car("Toyota", 500000)
c2 = Car("Honda", 700000)

c1.show()
c2.show()