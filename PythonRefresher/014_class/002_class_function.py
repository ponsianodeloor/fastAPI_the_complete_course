"""
POO
Object Oriented Programing
"""


class Student:
    university = 'ESPOL'

    def __init__(self, firstname, lastname, major):
        self.firstname = firstname
        self.lastname = lastname
        self.major = major

    def fullname_with_major(self):
        return f"{self.firstname} {self.lastname} major {self.major}"

    def fullname_major_school(self):
        if self.firstname == "Thomas":
            self.university = "UTB"
        return f"{self.firstname} " \
               f"{self.lastname} " \
               f"major {self.major} " \
               f"university {self.university}"

    @classmethod
    def set_online_school(cls, new_university):
        cls.university = new_university

    @classmethod
    def add_new_student(cls, student):
        firstname, lastname, major = student.split('.')
        # return cls(firstname=firstname, lastname=lastname, major=major)
        return cls(firstname, lastname, major)


student_1 = Student('Ponsiano', 'De Loor', 'Data Science')
student_2 = Student('Thomas', 'Sizalema', 'Sec Compute')

# print(student_1.firstname)
# print(student_2.lastname)
#
# print(student_1.fullname_with_major())
#
# print(student_1.university)
# print(student_2.university)
#
# print(student_1.fullname_major_school())
# print(student_2.fullname_major_school())
#
# print(student_1.university)
#
# student_1.set_online_school("UEM")
# print(student_1.university)
# print(student_2.university)
# print(student_2.fullname_major_school())

new_student_3 = 'Pon.Wick.Hacker'
new_student_4 = 'Thomas.BabaYaga.Hacker'

print(new_student_4.split("."))
student_3 = Student.add_new_student(new_student_3)
student_4 = Student.add_new_student(new_student_4)
print(student_3.fullname_major_school())
print(student_4.fullname_major_school())
