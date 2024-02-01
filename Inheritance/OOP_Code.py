# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
 
    def speak(self):
        pass
 
# Child classes
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
 
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
 
class Fox(Animal):
    def speak(self):
        return f"{self.name} says Ding Ding Ding Ding!"
   
 
# Creating objects
dog = Dog("Buddy")
cat = Cat("Whiskers")
fox = Fox("Swiper")
 
# Function demonstrating polymorphism
def animal_sound(animal):
    return animal.speak()
 
# Using polymorphism
animals = [dog, cat]
 
for animal in animals:
    print(animal_sound(animal))
 
# Using methods
print(dog.speak())
print(cat.speak())
print(fox.speak())
print(animal.speak)