# A Lecturer teaches one or more courses and is the person who records grades.
class Lecturer:
    def __init__(self, l_id, l_name, l_email):
        # Contact details for the lecturer.
        self.l_id = l_id
        self.l_name = l_name
        self.l_email = l_email

        # The courses this lecturer is responsible for. Starts empty and
        # fills up as they are assigned to teach things.
        self.courses = []

    def teach(self, course):
        # Link the lecturer and the course to each other, so each side
        # knows about the other.
        course.lecturer = self
        self.courses.append(course)

    def record_grade(self, student, course, grade):
        # A grade only makes sense if the student is actually in the course,
        # so check that first and back out politely if they are not.
        if student not in course.students:
            print(f"{student.s_name} is not enrolled in {course.code}, so no grade was saved.")
            return False

        # Store the grade against the course code on the student's record.
        student.grades[course.code] = grade
        return True

    def view_enrolled_students(self, course):
        # Nobody signed up yet? Let the user know and stop.
        if not course.students:
            print(f"No students enrolled in course: {course.code}.")
            return

        # List each enrolled student as "ID: Name".
        for student in course.students:
            print(f"{student.s_id}: {student.s_name}")
