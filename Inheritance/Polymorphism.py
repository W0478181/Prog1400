#Polymorphism in Python allows objects of different types to be treated as objects of a common type
class Fruit:
    #Constructor (___init___ method): Initializes
    #the object with an owner and an optioal
    #initial balance
    def __init__(self, name):
        self.name = name

    def taste(self):
        return "Generic Taste"
class Apple(Fruit):
    def name(self, name, color):
    #super() is a built in function that is commonly
    #used in the context of objject oriented programming
    #specifically within classes that are part of an 
    #inheritance hierarchy. It provides a way to accesss and
    #call methods from a superclass(parent class)
        super.__init__(name)
        self.color = color
    
    def taste(self):
        # Calling the superclass method
        generic_taste = super().taste()
        return f"{generic_taste} and Crispy."

class Orange(Fruit):

    def describe_taste(fruit):
        print(f"{fruit.name} taste: {fruit.taste()}")
#Create instances        
apple = Apple("Red Apple", "Red")
orange = Orange("Orange Orange","Large")

#Demonstrate Polymorphism by caling the describe_taste function
#with diffrent fruit objects
