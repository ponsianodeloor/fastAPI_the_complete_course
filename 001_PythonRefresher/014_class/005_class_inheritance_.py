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
    def __init__(self, firstname, lastname, major):
        super(CollegeStudent, self).__init__(firstname, lastname)
        self.major = major

    def greetings(self):
        return f" {self.firstname} {self.lastname} is a College Student"


class NonCollegeStudent(Student):
    def __init__(self, firstname, lastname, future_joob):
        super(NonCollegeStudent, self).__init__(firstname, lastname)
        self.future_job = future_joob

    def grow_up(self):
        return f"When i grow up, i want to be a {self.future_job}"


student_1 = Student('Ponsiano', 'De Loor Sizalema')
student_2 = Student('Thomas', 'Sizalema')

print(student_1.greetings())
print(student_2.greetings())

student_3 = CollegeStudent('Ponsiano', 'De Loor', 'Ms Compute Security')
print(student_3.greetings())
print(student_3.major)

student_4 = NonCollegeStudent('Thomas', 'De Loor', 'Ing de Sistemas')
print(student_4.grow_up())
