# polymorphism means same function name but different behavior
# operator overloading means using operators in custom way for objects

# program 1
# function polymorphism

class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

def make_sound(animal):
    animal.sound()

d = Dog()
c = Cat()

make_sound(d)
make_sound(c)


# program 2
# method overriding (polymorphism example)

class Parent:
    def show(self):
        print("\nThis is Parent class method")

class Child(Parent):
    def show(self):
        print("This is Child class method")

obj = Child()
obj.show()


# program 3
# operator overloading using + operator

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(10)
n2 = Number(20)

result = n1 + n2

print("\nSum using operator overloading:", result)