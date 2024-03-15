import math

class MarkManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    def input_marks(self, course_id, student_id, marks):
        for student in self.students:
            if student.student_id == student_id:
                student.add_marks(course_id, math.floor(marks))
                return True
        return False

    def calculate_student_gpa(self, student):
        return student.calculate_gpa(self.courses)

    def list_students(self):
        sorted_students = sorted(self.students, key=self.calculate_student_gpa, reverse=True)
        return sorted_students

    def list_courses(self):
        return self.courses

    def show_student_marks(self, course_id):
        marks_info = {}
        for student in self.students:
            if course_id in student.marks:
                marks_info[student.name] = student.marks[course_id]
        return marks_info
