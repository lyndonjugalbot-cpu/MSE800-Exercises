# Config holds two helpers that keep main.py tidy: one that fills the
# university with sample data, and one that prints the menu.
class Config:

    @staticmethod
    def populate_data(university):
        # Add a few lecturers.
        university.add_lecturer("L001", "Dr. Mohammad", "mohammad@yoobee.ac.nz")
        university.add_lecturer("L002", "Dr. Reem", "reem@yoobee.ac.nz")
        university.add_lecturer("L003", "Dr. Helena", "helena@yoobee.ac.nz")

        # Add a couple of students.
        university.add_student("S001", "Lyndon Jugalbot", "lyndon@yoobee.com")
        university.add_student("S002", "Sample Person", "sample@yoobee.com")

        # Add some courses. The last argument is the ID of the lecturer
        # who teaches that course.
        university.add_course("MSE800", "Software Engineering", 30, "L001")
        university.add_course("MSE801", "Research Methods", 20, "L002")
        university.add_course("MSE802", "Quantum Computing", 25, "L003")

        # Enrol the students in a few courses so there is something to see
        # straight away.
        university.students["S001"].enrol(university.courses["MSE800"])
        university.students["S002"].enrol(university.courses["MSE800"])
        university.students["S002"].enrol(university.courses["MSE801"])
        university.students["S001"].enrol(university.courses["MSE802"])

    @staticmethod
    def menu():
        # Just print the list of things the user can do.
        print("\nCollege Management System")
        print("1. Enrol student")
        print("2. View grades")
        print("3. Record grade")
        print("4. View students enrolled in course")
        print("5. Exit")
