

def display_students(stdscr, students):
    stdscr.clear()
    stdscr.addstr(0, 0, "List of Students:")
    for i, student in enumerate(students):
        stdscr.addstr(i + 1, 0, str(student))
    stdscr.refresh()

def display_courses(stdscr, courses):
    stdscr.clear()
    stdscr.addstr(0, 0, "List of Courses:")
    for i, course in enumerate(courses):
        stdscr.addstr(i + 1, 0, str(course))
    stdscr.refresh()

def display_student_marks(stdscr, marks_info):
    stdscr.clear()
    stdscr.addstr(0, 0, f"Student Marks for Course {course_id}:")
    for i, (name, mark) in enumerate(marks_info.items()):
        stdscr.addstr(i + 1, 0, f"{name}'s marks: {mark}")
    stdscr.refresh()
