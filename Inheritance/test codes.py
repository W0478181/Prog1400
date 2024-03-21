class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_grade(self, grade):
        self.grade = grade

    def get_grade(self):
        return self.grade


student1 = Student("Bryan", 18, "A")
print("Student 1:", student1.get_name(), student1.get_age(), student1.get_grade())

student2 = Student("Bob", 17, "B")
print("Student 2:", student2.get_name(), student2.get_age(), student2.get_grade())

student1.set_age(19)
student1.set_grade("C")

print("Updated Student 1:", student1.get_name(), student1.get_age(), student1.get_grade())
