#Aiden Connolly
#W0478181 
#Prog1400
#Project:Assignment 2
# Programming Language: Python 3

import math

#Task 1 Abstraction
print("\n Task 1")
#Defined a class named Shape
class Shape:
    def __init__(self):
        pass
#Method for area
    def area(self):
        pass
#Created two subclasses Rectangle and Circle that inherit from Shape 
#Each subclass overrides method for calculating area
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

rectangle = Rectangle(5, 10)
circle = Circle(3)

print("Area of Rectangle:", rectangle.area())
print("\nArea of Circle:", round(circle.area(),2))

#Task 2 Encapsulation
print("\n Task 2")
#Defined a class named Student with methods to get and set details
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def set_info(self):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_grade(self):
        return self.grade

student1 = Student()
#Will display student details
student1.set_info("Bryan", 20, 80)
print("\nStudent Info")
print("\nStudent Name:", student1.get_name())
print("\nStudent Age:", student1.get_age())
print("\nStudent Grade:", student1.get_grade())

#Input to change details manually
name = input("\nWhat is student name?:")
age = int(input("\nWhat is student age?:"))
grade = int(input("\nWhat is student grade?:"))
#Will set students new details
student1.set_info(name, age , grade)
#Will display student updated details
print("\nStudent Info")
print("\nStudent Name:", student1.get_name())
print("\nStudent Age:", student1.get_age())
print("\nStudent Grade:", student1.get_grade())

#Task 3  Inheritance 
print("\nTask 3")
#Defined a class named Animal with speak and move methods
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

    def move(self):
        pass
#Created subclasses Dog, Cat and Bird and override the pass to change for each animal 
class Dog(Animal):
    def speak(self):
        return f"\n{self.name} says Woof!"
    
    def move(self):
        return f"{self.name} is Running"
 
class Cat(Animal):
    def speak(self):
        return f"\n{self.name} says Meow!"
    
    def move(self):
        return f"{self.name} is Sleeping"
 
class Bird(Animal):
    def speak(self):
        return f"\n{self.name} says Tweet Tweet!"
    
    def move(self):
        return f"{self.name} is Flying"

dog = Dog("Jaxx")
cat = Cat("Sylvester")
bird = Bird("Tweety")

print(dog.speak())
print(dog.move())

print(cat.speak())
print(cat.move())

print(bird.speak())
print(bird.move())

#Task 4 Polymorphism
print("\nTask 4")
#Defined a class named Vehicle with travel method
class Vehicles:
    def __init__(self):
        pass

    def travel():
        print("\n The vehicle is travelling.")
#Subclasses that override the travel method
class Cars(Vehicles):
    def travel(self):
        print("\nCars drive on roads.")

class Planes(Vehicles):
    def travel(self):
        print("\nPlanes fly in the air.")

class Bikes(Vehicles):
    def travel(self):
        print("\nBikes travel on roads and paths.")
#Polymorphism    
def vehicle_travel(Vehicles):
    Vehicles.travel()

car = Cars()
plane = Planes()
bike = Bikes()

vehicle_travel(car)
vehicle_travel(plane)
vehicle_travel(bike)
