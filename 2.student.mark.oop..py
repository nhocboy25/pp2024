class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def add_marks(self, course_id, marks):
        self.marks[course_id] = marks

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, DoB: {self.dob}"

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

    def __str__(self):
        return f"ID: {self.course_id}, Name: {self.name}"

class MarkManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    def input_marks(self):
        course_id = input("Enter course ID to input marks: ")
        for student in self.students:
            marks = float(input(f"Enter marks for {student.name}: "))
            student.add_marks(course_id, marks)

    def list_students(self):
        print("List of Students:")
        for student in self.students:
            print(student)

    def list_courses(self):
        print("List of Courses:")
        for course in self.courses:
            print(course)

    def show_student_marks(self):
        course_id = input("Enter course ID to show student marks: ")
        for student in self.students:
            if course_id in student.marks:
                print(f"{student.name}'s marks for {course_id}: {student.marks[course_id]}")

if __name__ == "__main__":
    mark_system = MarkManagementSystem()

    num_students = int(input("Enter the number of students in the class: "))
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        student = Student(student_id, name, dob)
        mark_system.add_student(student)

    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        course = Course(course_id, name)
        mark_system.add_course(course)

    while True:
        print("\nOptions:")
        print("1. Input Marks")
        print("2. List Students")
        print("3. List Courses")
        print("4. Show Student Marks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            mark_system.input_marks()
        elif choice == "2":
            mark_system.list_students()
        elif choice == "3":
            mark_system.list_courses()
        elif choice == "4":
            mark_system.show_student_marks()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
