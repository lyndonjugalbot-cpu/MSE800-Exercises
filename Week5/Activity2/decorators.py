# Decorators that enforce a rule before a method runs.
import functools


def require_enrolled(method):
    # Runs the "is the student in the course?" check before record_grade.
    # This is the «include» check from the use case diagram.
    @functools.wraps(method)
    def wrapper(self, student, course, grade):
        # Not enrolled: say why and stop here.
        if student not in course.students:
            print(f"{student.s_name} is not enrolled in {course.code}, so no grade was saved.")
            return False

        # Enrolled: run the real method.
        return method(self, student, course, grade)

    return wrapper
