"""
POO
Object Oriented Programing - Inheritance
"""


class Student:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def greetings(self):
        return f" Hello Im {self.firstname} {self.lastname}"

# Esta clase hereda de Student por lo tanto tiene todos los metodos y propiedades
class CollegeStudent(Student):
    pass


student_1 = Student('Ponsiano', 'De Loor')
student_2 = Student('Thomas', 'Sizalema')

print(student_1.greetings())
print(student_2.greetings())

student_3 = CollegeStudent('Ponsiano', 'De Loor')
print(student_3.greetings())
