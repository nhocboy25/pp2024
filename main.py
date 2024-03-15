
from student import Student
from course import Course
from mark_management import MarkManagementSystem
from input import input_students, input_courses, input_marks
from output import display_students, display_courses, display_student_marks

def main(stdscr):
    mark_system = MarkManagementSystem()

    students = input_students()
    courses = input_courses()

    for student_id, name, dob in students:
        mark_system.add_student(Student(student_id, name, dob))

    for course_id, name, credits in courses:
        mark_system.add_course(Course(course_id, name, credits))

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
            course_id, marks = input_marks(students)
            mark_system.input_marks(course_id, marks)
        elif choice == "2":
            display_students(stdscr, mark_system.list_students())
        elif choice == "3":
            display_courses(stdscr, mark_system.list_courses())
        elif choice == "4":
            course_id = input("Enter course ID to show student marks: ")
            display_student_marks(stdscr, mark_system.show_student_marks(course_id))
        elif choice == "5":
            break
        else:
            stdscr.addstr(7, 0, "Invalid choice. Please enter a number between 1 and 5.")
