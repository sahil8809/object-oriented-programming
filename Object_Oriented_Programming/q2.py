class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        else:
            return "C"
s1 = Student("Riya", 88)
print(s1.name, "got grade", s1.grade())
