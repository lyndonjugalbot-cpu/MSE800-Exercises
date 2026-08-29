from student import Student
from lecturer import Lecturer
from course import Course


# The University ties everything together. It keeps three simple lookup
# tables (dictionaries) so we can find any student, lecturer or course by ID.
class University:
    def __init__(self):
        self.students = {}    # {student_id: Student}
        self.lecturers = {}   # {lecturer_id: Lecturer}
        self.courses = {}     # {course_code: Course}

    def add_student(self, s_id, s_name, s_email):
        # Create a Student and file it under their ID.
        self.students[s_id] = Student(s_id, s_name, s_email)

    def add_lecturer(self, l_id, l_name, l_email):
        # Create a Lecturer and file them under their ID.
        self.lecturers[l_id] = Lecturer(l_id, l_name, l_email)

    def add_course(self, code, course_name, credits, l_id):
        # Build the course, store it, then hand it to the lecturer who
        # will be teaching it.
        course = Course(code, course_name, credits)
        self.courses[code] = course
        self.lecturers[l_id].teach(course)
