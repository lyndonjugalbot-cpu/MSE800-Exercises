"""Demo for the university class hierarchy.

Shows inheritance in action and answers the two questions from the brief:
  * number of publications for a lecturer  (Academic)
  * pay rate for a general staff member    (General)
"""

from university import Student, General, Academic


def main():
    # --- Build some objects -------------------------------------------------
    student = Student(id=1, name="Ava Chen", student_id="S1001")

    general = General(
        id=2,
        name="Ben Rata",
        staff_id="G1234",
        tax_num="TX-12345",
        hourly_rate=30,
        hours_worked=40,
    )

    lecturer = Academic(
        id=3,
        name="Dr. Mohammad",
        staff_id="A1234",
        tax_num="TX-7890",
        publications=[
            "Sofware ENgineering",
            "A study of Python",
        ],
    )
    lecturer.add_publication("Teaching OOP with Python")

    # --- Inheritance / polymorphism --------------------------------------
    print("=== People at the university ===")
    for person in (student, general, lecturer):
        print("-", person)          # uses Person.__str__ -> describe()

    # --- Number of publications for a lecturer ----------------------------
    print("\n=== Lecturer publications ===")
    lecturer.display_publications()

    # --- Pay rate for a general staff member -----------------------------
    print("\n=== General staff pay ===")
    general.display_pay_rate()


if __name__ == "__main__":
    main()
