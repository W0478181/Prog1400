#Class
'''Constructor method (__innit__)
    contructor initializes the objects attributes
    EX.it sets brand,model and engine status
'''
#Contructure method
class car:
    def __init__(self, brand, model, colour):
        self.brand = brand
        self.model = model
        self.colour = colour
        self.is_running = False
    '''
    Methods:Functions inside a class are called methods.
    start_engine and stop_engine are methids of the car class.
    '''    
    #Method to Start Car    
    def start_engine(self):
        self.is_running = True
        print(f"The {self.brand} {self.model}'s engine is running.")
    #Method to Shut off Car    
    def stop_engine(self):
        self.is_running = False
        print(f"The {self.brand} {self.model}'s engine is off.")
    '''
    Objects:Objects are instances of a class.
    car1 and car2 are instances of the clas car
    '''

#Object Oriented Approach
#Create an instant of the class by creating object
car1 = car("Nissan", "Sentra", "Black")
car2 = car("Honda", "Civic", "Red")

car1.start_engine()
car1.stop_engine()

print(car1.brand,car1.model,car1.colour)

#List
car_1 = ["Nissan", "Sentra", "Black"]
car_2 = ["Honda", "Civic", "Red"]



