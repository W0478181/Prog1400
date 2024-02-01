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

    
my_rectangle  = Rectangle(length=5, width=3, height=6)

print(f"Length: {my_rectangle.length}")
print(f"Width: {my_rectangle.width}")
print(f"Height: {my_rectangle.height}")

surface_area = my_rectangle.calculate_surface_area()
volume = my_rectangle.calculate_volume()
print("Surface Area:",surface_area)
print("Volume:",volume)


