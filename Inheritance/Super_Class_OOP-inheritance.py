import math


# Create a rectangle and define attributes and methods: calculate_area and calculate_perimeter
# Step 1: Define the Class -Classes are templates for objects
# Rectangle is the name of the class
# __init__ is a special method called the contructor, used to initialize the objects attributes
# Length and width are attributes of the class
# Calculate_area and calculate_perimeter are methods that perform calculations based on the attributes

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 *(self.length + self.width)
    

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(length = side_length, width = side_length)
    
# Step 2: Create a object
# Creating an instance of the Rectangle class
# Create an instance my_rectangle of 
    
my_rectangle  = Rectangle(length = 5, width = 3)

my_square = Square(side_length = 5)
# Step 3 Accesing Object Attributes
# We use dot notation (object.attribute) to access the attributes of the my_rectangle object
print(f"Rectangle Length: {my_rectangle.length}")
print(f"Rectangle Width: {my_rectangle.width}")

area = my_rectangle.calculate_area()
perimeter = my_rectangle.calculate_perimeter()
print("\nRectangle Area:",area)
print("Rectangle Perimeter:",perimeter)

print("\nSquare Side Length:",my_square.length)
print("Square Side Width:",my_square.width)
# Step 4: Calling Object Methods
# We call the methods calculate_area and calculate_perimeter of the my_rectangle object
area_square = my_square.calculate_area()
perimeter_square = my_square.calculate_perimeter()

print("\nSquare Perimeter:",perimeter_square)
print("Square Area:",area_square)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.pi * (self.radius * self.radius)
    
    def calculate_perimeter(self):
        return 2 *(self.pi * self.radius)
    
my_circle = Circle(radius = 5, pi = math.pi)

print(f"\nCircle Radius: {my_circle.radius}")

area_circle = my_circle.calculate_area()
perimeter_circle = my_circle.calculate_perimeter()
print("\nCircle Area:",round(area_circle,2))
print("Circle Perimeter:",round(perimeter_circle,2))
