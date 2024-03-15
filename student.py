class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def add_marks(self, course_id, marks):
        # Round down to 1-digit decimal using math.floor
        self.marks[course_id] = marks

    def calculate_gpa(self, courses):
        total_credits = sum(course.credits for course in courses)
        weighted_sum = sum(self.marks.get(course.course_id, 0) * course.credits for course in courses)
        if total_credits == 0:
            return 0
        return weighted_sum / total_credits

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, DoB: {self.dob}, GPA: {self.gpa:.2f}"
