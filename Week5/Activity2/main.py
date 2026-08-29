# This is where the program starts. Run this file to use the
# College Management System from the terminal.

from university import University
from config import Config


def find(collection, key, label):
    # A small helper so a mistyped ID doesn't blow up the whole program.
    # If the key is there we return the object; if not, we explain what
    # went wrong and return None so the caller can stop early.
    if key in collection:
        return collection[key]
    print(f"{label} '{key}' was not found. Please check the ID and try again.")
    return None


def main():
    # Start with an empty university, then load the sample data so there
    # is something to work with right away.
    university = University()
    Config.populate_data(university)

    # Keep showing the menu until the user picks "Exit".
    while True:
        Config.menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            # Enrol a student into a course.
            student = find(university.students, input("Student ID: ").strip(), "Student")
            course = find(university.courses, input("Course Code: ").strip(), "Course")
            if student and course:
                if student.enrol(course):
                    print(f"{student.s_name} is now enrolled in {course.code}.")
                else:
                    print(f"{student.s_name} is already enrolled in {course.code}.")

        elif choice == "2":
            # Show every grade a student has so far.
            student = find(university.students, input("Student ID: ").strip(), "Student")
            if student:
                student.view_grades()

        elif choice == "3":
            # A lecturer records a grade for a student in one course.
            lecturer = find(university.lecturers, input("Lecturer ID: ").strip(), "Lecturer")
            student = find(university.students, input("Student ID: ").strip(), "Student")
            course = find(university.courses, input("Course Code: ").strip(), "Course")
            if lecturer and student and course:
                grade = input("Grade: ").strip()
                if lecturer.record_grade(student, course, grade):
                    print("Grade recorded!")

        elif choice == "4":
            # List everyone enrolled in a given course.
            lecturer = find(university.lecturers, input("Lecturer ID: ").strip(), "Lecturer")
            course = find(university.courses, input("Course Code: ").strip(), "Course")
            if lecturer and course:
                lecturer.view_enrolled_students(course)

        elif choice == "5":
            # Break out of the loop, which ends the program.
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


# Only run main() when this file is executed directly, not when imported.
if __name__ == "__main__":
    main()
