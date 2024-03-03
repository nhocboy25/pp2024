import curses
import math
import numpy as np

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def add_marks(self, course_id, marks):
        # Round down to 1-digit decimal using math.floor
        self.marks[course_id] = math.floor(marks)

    def calculate_gpa(self, courses):
        total_credits = sum(course.credits for course in courses)
        weighted_sum = sum(self.marks.get(course.course_id, 0) * course.credits for course in courses)
        if total_credits == 0:
            return 0
        return weighted_sum / total_credits

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, DoB: {self.dob}, GPA: {self.gpa:.2f}"

class Course:
    def __init__(self, course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits

    def __str__(self):
        return f"ID: {self.course_id}, Name: {self.name}, Credits: {self.credits}"

class MarkManagementSystem:
    def __init__(self, stdscr):
        self.students = []
        self.courses = []
        self.stdscr = stdscr

    def input_students(self):
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "Enter the number of students in the class: ")
        self.stdscr.refresh()
        num_students = int(self.stdscr.getstr().decode())

        for i in range(num_students):
            self.stdscr.clear()
            self.stdscr.addstr(0, 0, f"Enter details for student {i + 1}:")
            self.stdscr.addstr(1, 0, "ID: ")
            self.stdscr.addstr(2, 0, "Name: ")
            self.stdscr.addstr(3, 0, "DoB: ")
            self.stdscr.refresh()

            student_id = self.stdscr.getstr().decode()
            name = self.stdscr.getstr().decode()
            dob = self.stdscr.getstr().decode()

            student = Student(student_id, name, dob)
            self.students.append(student)

    def input_courses(self):
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "Enter the number of courses: ")
        self.stdscr.refresh()
        num_courses = int(self.stdscr.getstr().decode())

        for i in range(num_courses):
            self.stdscr.clear()
            self.stdscr.addstr(0, 0, f"Enter details for course {i + 1}:")
            self.stdscr.addstr(1, 0, "ID: ")
            self.stdscr.addstr(2, 0, "Name: ")
            self.stdscr.addstr(3, 0, "Credits: ")
            self.stdscr.refresh()

            course_id = self.stdscr.getstr().decode()
            name = self.stdscr.getstr().decode()
            credits = int(self.stdscr.getstr().decode())

            course = Course(course_id, name, credits)
            self.courses.append(course)

    def input_marks(self):
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "Enter course ID to input marks: ")
        self.stdscr.refresh()
        course_id = self.stdscr.getstr().decode()

        for student in self.students:
            self.stdscr.clear()
            self.stdscr.addstr(0, 0, f"Enter marks for {student.name}: ")
            self.stdscr.refresh()

            marks = float(self.stdscr.getstr().decode())
            student.add_marks(course_id, marks)

    def calculate_student_gpa(self, student):
        return student.calculate_gpa(self.courses)

    def list_students(self):
        sorted_students = sorted(self.students, key=self.calculate_student_gpa, reverse=True)
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "List of Students:")
        for i, student in enumerate(sorted_students):
            self.stdscr.addstr(i + 1, 0, str(student))
        self.stdscr.refresh()

    def list_courses(self):
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "List of Courses:")
        for i, course in enumerate(self.courses):
            self.stdscr.addstr(i + 1, 0, str(course))
        self.stdscr.refresh()

    def show_student_marks(self):
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "Enter course ID to show student marks: ")
        self.stdscr.refresh()
        course_id = self.stdscr.getstr().decode()

        self.stdscr.clear()
        self.stdscr.addstr(0, 0, f"Student Marks for Course {course_id}:")
        for i, student in enumerate(self.students):
            if course_id in student.marks:
                self.stdscr.addstr(i + 1, 0, f"{student.name}'s marks: {student.marks[course_id]}")
        self.stdscr.refresh()

def main(stdscr):
    mark_system = MarkManagementSystem(stdscr)

    mark_system.input_students()
    mark_system.input_courses()

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Options:")
        stdscr.addstr(1, 0, "1. Input Marks")
        stdscr.addstr(2, 0, "2. List Students")
        stdscr.addstr(3, 0, "3. List Courses")
        stdscr.addstr(4, 0, "4. Show Student Marks")
        stdscr.addstr(5, 0, "5. Exit")
        stdscr.addstr(6, 0, "Enter your choice (1-5): ")
        stdscr.refresh()

        choice = stdscr.getstr().decode()

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
            stdscr.addstr(7, 0, "Invalid choice. Please enter a number between 1 and 5.")
            stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)
