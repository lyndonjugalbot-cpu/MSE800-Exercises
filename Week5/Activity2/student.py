# A Student is a person who enrols in courses and collects grades along the way.
class Student:
    def __init__(self, s_id, s_name, s_email):
        # The basic contact details we were given when the student joined.
        self.s_id = s_id
        self.s_name = s_name
        self.s_email = s_email

        # Grades start out empty. We store them as {course_code: grade},
        # for example {"MSE800": "A"}. This line was missing before, which
        # is why viewing grades used to crash.
        self.grades = {}

    def enrol(self, course):
        # Enrolling really just means "add me to that course's list".
        # We let the course handle the details and pass back whatever it
        # tells us (True if it worked, False if we were already on the list).
        return course.enrol_student(self)

    def view_grades(self):
        # If nothing has been graded yet, say so plainly and stop here.
        if not self.grades:
            print(f"No grades available yet for {self.s_name}.")
            return

        # Otherwise walk through each course and print its grade.
        for course_code, grade in self.grades.items():
            print(f"{course_code}: {grade}")
