from enum import Enum

class Grade(Enum):
    A = 90
    B = 75
    C = 50
    D = 35
    F = 0

class Student:
    def __init__(self, name, marks=None):
        self.name = name
        self.marks = marks if marks is not None else [25]

    def calculate_percentage(self):
        return sum(self.marks) // len(self.marks)

    def find_grade(self):
        percentage = self.calculate_percentage()
        for grade in Grade:
            if percentage >= grade.value:
                return grade.name



s1 = Student("Sai", [85, 90, 80])
print("Name:", s1.name)
print("Percentage:", s1.calculate_percentage())
print("Grade:", s1.find_grade())

s2 = Student("Kumar")
print("\nName:", s2.name)
print("Percentage:", s2.calculate_percentage())
print("Grade:", s2.find_grade())

s2.marks = [60, 70, 65]
print("\nUpdated Marks:", s2.marks)
print("Updated Percentage:", s2.calculate_percentage())
print("Updated Grade:", s2.find_grade())
