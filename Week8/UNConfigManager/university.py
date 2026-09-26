    
class UniversityConfig: 
    _instance = None 

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.university_name = None
            cls._instance.academic_year = None
            cls._instance.semester = None
        return cls._instance

    def set_config(self, university_name, academic_year, semester):
        self.university_name = university_name
        self.academic_year = academic_year
        self.semester = semester

    def display_config(self):
        print(f"University: {self.university_name}")
        print(f"Academic Year: {self.academic_year}")
        print(f"Semester: {self.semester}")