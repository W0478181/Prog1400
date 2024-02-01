class animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat
    
    def speak(self):
        pass

#Child class or sub class
class Dog(animal):
    def speak(self):
        return f"{self.name} says Woof."
    def habitat(self):
        return f"{self.name} is Domestic."
    
class Cat(animal):
    def speak(self):
        return f"{self.name} says Meow."
    def habitat(self):
        return f"{self.name} is Domestic."
    
'''
Objects:Objects are instances of a class.
dog and cat are instances of the dog and cat sub classes which inherits
the animal class
'''
#Create Object
dog1 = Dog("Jaxx","Domestic")
cat1 = Cat("Rubin","Domestic")

#Using methods
print(Dog.speak(dog1), Dog.habitat(dog1))
print(Cat.speak(cat1), Cat.habitat(cat1))

