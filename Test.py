class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")

    def update_grade(self, new_grade):
        self.grade = new_grade


class GraduateStudent(Student):
    def __init__(self, student_id, name, age, grade, thesis_topic):
        super().__init__(student_id, name, age, grade)
        self.thesis_topic = thesis_topic

    def display_info(self):
        super().display_info()
        print(f"Thesis Topic: {self.thesis_topic}")


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_all_students(self):
        for student in self.students:
            student.display_info()
            print()

    def search_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                student.display_info()
                return
        print("Student not found.")

    def update_grade_by_id(self, student_id, new_grade):
        for student in self.students:
            if student.student_id == student_id:
                student.update_grade(new_grade)
                print("Grade updated successfully.")
                return
        print("Student not found.")


# Demonstration
def main():
    sms = StudentManagementSystem()

    # Adding students
    student1 = Student(1, "Alice", 20, 85.5)
    student2 = GraduateStudent(2, "Bob", 25, 78.3, "Machine Learning")
    sms.add_student(student1)
    sms.add_student(student2)

    # Displaying all students
    print("\nAll Students:\n")
    sms.display_all_students()

    # Searching for a student by ID
    print("Searching for student with ID 2:\n")
    sms.search_student_by_id(2)

    # Updating grade of a student by ID
    print("\nUpdating grade of student with ID 1:\n")
    sms.update_grade_by_id(1, 90)
    sms.search_student_by_id(1)


if __name__ == "__main__":
    main()
