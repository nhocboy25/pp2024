def input_students():
    num_students = int(input("Enter the number of students in the class: "))
    students = []
    for i in range(num_students):
        student_id = input(f"Enter student {i+1} ID: ")
        name = input(f"Enter student {i+1} name: ")
        dob = input(f"Enter student {i+1} date of birth: ")
        students.append((student_id, name, dob))
    return students

def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    courses = []
    for i in range(num_courses):
        course_id = input(f"Enter course {i+1} ID: ")
        name = input(f"Enter course {i+1} name: ")
        credits = int(input(f"Enter course {i+1} credits: "))
        courses.append((course_id, name, credits))
    return courses

def input_marks(students):
    course_id = input("Enter course ID to input marks: ")
    marks = {}
    for student in students:
        student_id = student[0]
        mark = float(input(f"Enter marks for {student[1]} ({student_id}): "))
        marks[student_id] = mark
    return course_id, marks
