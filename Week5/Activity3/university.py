"""Class hierarchy of university people.

Person ->Student
Person ->Staff
Staff ->General (general staff - paid by an hourly rate)
Staff ->Academic (academic staff - assessed on publication)
"""

from abc import ABC, abstractmethod


class Person(ABC):
    """Base class for every person at the university."""

    def __init__(self, id, name):
        self.id = id
        self.name = name

    @abstractmethod
    def describe(self):
        """Return a short human-readable summary of the person."""
        raise NotImplementedError

    def __str__(self):
        return self.describe()

class Student(Person):
    """A person enrolled to study."""
    def __init__(self, id, name, student_id):
        super().__init__(id,name)
        self.student_id = student_id

    def describe(self):
        return f"Student{self.name} (student_id={self.student_id})"
    

class Staff(Person):
    """A person employed by the university."""
    def __init__(self, id, name, staff_id, tax_num):
        super().__init__(id, name)
        self.staff_id = staff_id
        self.tax_num = tax_num

    def describe(self):
        return f"Staff {self.name} (staff_id={self.staff_id})"


class General(Staff):
    """General staff member paid according to an hourly pay rate."""

    def __init__(self, id, name, staff_id, tax_num, hourly_rate, hours_worked=0):
        super().__init__(id, name, staff_id, tax_num)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay_rate(self):
        """Calculate the gross pay for the hours worked."""
        return self.hourly_rate * self.hours_worked

    def display_pay_rate(self):
        pay = self.calculate_pay_rate()
        print(
            f"{self.name} (general staff): {self.hours_worked} h "
            f"x ${self.hourly_rate:.2f}/h = ${pay:.2f}"
        )
        return pay

    def describe(self):
        return f"General staff {self.name} (staff_id={self.staff_id})"


class Academic(Staff):
    """Academic staff member (lecturer) assessed on their publications."""

    def __init__(self, id, name, staff_id, tax_num, publications=None):
        super().__init__(id, name, staff_id, tax_num)
        self.publications = list(publications) if publications else []

    def add_publication(self, title):
        """Record a new publication for this lecturer."""
        self.publications.append(title)

    def calculate_publications(self):
        """Calculate the number of publications for this lecturer."""
        return len(self.publications)

    def display_publications(self):
        count = self.calculate_publications()
        print(f"{self.name} (lecturer) has {count} publication(s):")
        for i, title in enumerate(self.publications, start=1):
            print(f"  {i}. {title}")
        return count

    def describe(self):
        return f"Academic staff {self.name} (staff_id={self.staff_id})"
