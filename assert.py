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

# -------- Testing using assert --------

s1 = Student("Sai", [85, 90, 80])
assert s1.calculate_percentage() == 85
assert s1.find_grade() == "B"

s2 = Student("Kumar")
assert s2.calculate_percentage() == 25
assert s2.find_grade() == "F"

s2.marks = [60, 70, 65]
assert s2.calculate_percentage() == 65
assert s2.find_grade() == "B"

print("All test cases passed!")
