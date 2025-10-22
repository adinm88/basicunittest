"""
* Name         : <student.py>
* Author       : <Adin Mujakovic>
* Created      : <10/22/2025>
* Course       : CIS189
* IDE          : <Visual Studio Code>
* Description  : <Defines a Student class with properties and validation.>
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""
class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa
    
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(value)):
            raise ValueError ("Last name contains invalid characters.")
        self._last_name = str(value)
    
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(value)):
            raise ValueError ("First name contains invalid characters.")
        self._first_name = str(value)
    
    @property
    def major(self):
        return self._major
    
    @major.setter
    def major(self, value):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '-")
        if not (name_characters.issuperset(value)):
            raise ValueError ("Major contains invalid characters.")
        self._major = str(value)
    
    @property
    def gpa(self):
        return self._gpa
    
    @gpa.setter
    def gpa(self, value):
        if not isinstance(value, float):
            raise ValueError ("GPA must be a float.")
        if not (0.0 <= value <= 4.0):
            raise ValueError ("GPA must be between 0.0 and 4.0.")
        self._gpa = float(value)

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)

def main():
    student = Student("Doe", "John", "Computer Science", 3.5)
    print(student)
    student2 = Student("Smith", "Jane", "Biology", 4.0)
    print(student2)
    del student
    del student2

if __name__ == "__main__":
    main()