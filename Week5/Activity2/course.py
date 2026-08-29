# A Course is a single subject students can enrol in, taught by one lecturer.
class Course:
    def __init__(self, code, course_name, credits):
        # What the course is called and how much it is worth.
        self.code = code
        self.course_name = course_name
        self.credits = credits

        # Filled in later: the lecturer teaching it, and the list of
        # students who have enrolled.
        self.lecturer = None
        self.students = []

    def enrol_student(self, student):
        # If the student is already on the list, there is nothing to do.
        # Report back False so the caller can show a friendly message.
        if student in self.students:
            return False

        # Otherwise add them and report success.
        self.students.append(student)
        return True
