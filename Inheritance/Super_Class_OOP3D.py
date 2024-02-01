# 3D Rectangle

class Rectangle:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def calculate_surface_area(self):
        return 2 * ((self.length * self.width) +(self.length * self.height) + (self.height * self.width))
    
    def calculate_volume(self):
        return self.length * self.width * self.height

class Cube(Rectangle):
    def __init__(self, side_length):
        super().__init__(length = side_length, width = side_length, height = side_length)

my_rectangle  = Rectangle(length=5, width=3, height=6)
my_cube = Cube(side_length = 5)

print(f"Length: {my_rectangle.length}")
print(f"Width: {my_rectangle.width}")
print(f"Height: {my_rectangle.height}")

surface_area = my_rectangle.calculate_surface_area()
volume = my_rectangle.calculate_volume()
print("Surface Area:",surface_area)
print("Volume:",volume)

print("Square Side Length:",my_cube.length)
print("Square Side Width:",my_cube.width)
print("Square Side Heigth:",my_cube.height)

surface_area_cube = my_cube.calculate_surface_area()
volume_cube = my_cube.calculate_volume()
print("Perimeter of Square:",volume_cube)
print("Area of Square:",surface_area_cube)
