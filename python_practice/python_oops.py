#constructor
class Person:
    def __init__(self, name, age):  
        self.name = name
        self.age = age

p1 = Person("Hemant", 21)
print(p1.name, p1.age)


#self & comaprison
class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def __eq__(self, other):  
        return self.brand == other.brand and self.price == other.price

car1 = Car("Toyota", 20000)
car2 = Car("Toyota", 20000)
print(car1 == car2)  

#variables
class Student:
    school_name = "XYZ"  # Class Variable

    def __init__(self, name, grade):
        self.name = name  # Instance Variable
        self.grade = grade

    def display(self):
        local_var = "Local Variable"  # Local Variable
        print(self.name, self.grade, self.school_name, local_var)

s1 = Student("John", "A")
s1.display()


#method
class Employee:
    company = "Shorthills"  # Class Variable

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):  # Instance Method
        print(f"Employee {self.name} earns {self.salary}")

    @classmethod
    def change_company(cls, new_name):  # Class Method
        cls.company = new_name

    @staticmethod
    def info():  # Static Method
        print("Hello I am here")

e1 = Employee("Alex", 50000)
e1.show_details()
Employee.change_company("Shorthills2")
Employee.info()

#inner class
class Outer:
    class Inner:
        def display(self):
            print("Inside Inner Class")

o = Outer()
i = o.Inner()
i.display()


#inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
d.bark()


#constructor in inheritance
class Parent:
    def __init__(self, name):
        self.name = name
        print(f"Parent constructor: {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name) 
        self.age = age
        print(f"Child constructor: {self.name}, Age: {self.age}")

c = Child("Tom", 10)


#polymorphism
class Bird:
    def make_sound(self):
        print("Chirp Chirp")

class Dog:
    def make_sound(self):
        print("Bark Bark")

def animal_sound(animal):
    animal.make_sound()

b = Bird()
d = Dog()
animal_sound(b)
animal_sound(d)


#Duck Typing
class Sparrow:
    def fly(self):
        print("Sparrow can fly")

class Airplane:
    def fly(self):
        print("Airplane can fly")

def flight_test(flying_obj):
    flying_obj.fly()

s = Sparrow()
a = Airplane()
flight_test(s)
flight_test(a)


#operator overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2
print(p3.x, p3.y) 


#method overloading
class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c  

m = MathOperations()
print(m.add(1, 2))
print(m.add(1, 2, 3))


#method overriding
class Parent:
    def show(self):
        print("Parent class")

class Child(Parent):
    def show(self):  
        print("Child class")

c = Child()
c.show()  
