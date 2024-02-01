# 2D Shapes
import math

class Shape2D:
    def __init__(self):
        pass
    
    def area(self):
        pass
    def perimeter(self):
        pass
    def surface_area(self):
        pass
    def radius(self):
        pass
    def volume(self):
        pass

class Rectangle(Shape2D):
    def __init__(self, length, width, height):
        super().__init__(cuboid_length = length, cuboid_width = width, cuboid_height = height)

    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area_rectangle(self):
        return self.length * self.width

    def perimeter_rectangle(self):
        return 2 *(self.length + self.width)

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(length = side_length, width = side_length)

class Circle(Shape2D):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    def area_circle(self):
        return math.pi * (self.radius ** 2)
    
    def perimeter_circle(self):
        return 2 *(math.pi * self.radius)

class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius, height)
   
my_rectangle  = Rectangle(length = 5, width = 3)
my_square = Square(side_length = 5)
my_circle = Circle(radius = 5)

print(f"\nRectangle Length: {my_rectangle.length}")
print(f"Rectangle Width: {my_rectangle.width}")

area = my_rectangle.area_rectangle()
perimeter = my_rectangle.perimeter_rectangle()
print("\nRectangle Area:",area)
print("Rectangle Perimeter:",perimeter)

print("\nSquare Side Length:",my_square.length)
print("Square Side Width:",my_square.width)

area_square = my_square.area_rectangle()
perimeter_square = my_square.perimeter_rectangle()

print(f"\nCircle Radius: {my_circle.radius}")

area_circle = my_circle.area_circle()
perimeter_circle = my_circle.perimeter_circle()
print("\nCircle Area:",round(area_circle,2))
print("Circle Perimeter:",round(perimeter_circle,2))

# 3D Shapes

class Shape3D:
    def __init__(self):
        pass
    
    def area(self):
        pass
    def perimeter(self):
        pass
    def surface_area(self):
        pass
    def radius(self):
        pass
    def volume(self):
        pass

class Cuboid(Shape3D):
    def __init__(self, length, width, height):
        super().__init__(cuboid_length = length, cuboid_width = width, cuboid_height = height)

    def __init__(self, length, width, height):
        super().__init__()
        self.length = length
        self.width = width
        self.height = height

    def surface_area_cuboid(self):
        return 2 * ((self.length * self.width) + (self.length * self.height) + (self.height * self.width))

    def volume_cuboid(self):
        return self.length * self.width * self.height

class Cube(Cuboid):
    def __init__(self, side_length):
        super().__init__(length = side_length, width = side_length, height = side_length)

class Sphere(Shape3D):
    def __init__(self, radius):
        self.radius = radius

    def surface_area_sphere(self):
        return 4 * math.pi * (self.radius ** 2)
    
    def volume_sphere(self):
        return (4/3) * (math.pi * (self.radius ** 3))
    
my_cuboid = Cuboid(length = 5, width = 3, height = 6)
my_cube = Cube(side_length = 5)
my_sphere = Sphere(radius = 5)

print("\nCuboid Length:", my_cuboid.length)
print("Cuboid Width:", my_cuboid.width)
print("Cuboid Height:", my_cuboid.height)

surface_area_cuboid = my_cuboid.surface_area_cuboid()
volume_cuboid = my_cuboid.volume_cuboid()

print("\nCuboid Surface Area:", surface_area_cuboid)
print("Cuboid Volume:", volume_cuboid)

print("\nCube Length:", my_cube.length)
print("Cube Width:", my_cube.width)
print("Cube Height:", my_cube.height)

surface_area_cube = my_cube.surface_area_cuboid()
volume_cube = my_cube.volume_cuboid()

print("\nCube Surface Area:", surface_area_cube)
print("Cube Volume:", volume_cube)

print("\nSphere Height:", my_sphere.radius)

surface_area_sphere = my_sphere.surface_area_sphere()
volume_sphere = my_sphere.volume_sphere()

print("\nSphere Surface Area:",round(surface_area_sphere,2))
print("Sphere Volume:",round(volume_sphere,2))