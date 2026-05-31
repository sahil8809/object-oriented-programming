# class Student:
#     def __init__(self, name, age, marks):
        
#         self.name = name
        
#         try:
#             self.age = int(age)
#         except ValueError:
#             print("Invalid age! Setting to 0")
#             self.age = 0

#         try:
#             self.marks = int(marks)
#         except ValueError:
#             print("Invalid marks! Setting to 0")
#             self.marks = 0


# s1 = Student("Riya",19, 88)
# s2 = Student("Laila",17,77)
# s3 = Student("shaktimaan",60,49)
# s4 = Student("Thor",26,89)

# s = [s1,s2,s3,s4]
# for i in s:
#     print("name =", i.name)
#     print("marks =", i.marks)
#     print("age =", i.age)
#     print(80*"-")