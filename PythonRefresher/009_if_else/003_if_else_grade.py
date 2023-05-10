"""
Create a variable (grade) holding an ineger between 0 - 100
A = 90 - 100
B = 80 - 89
C = 70 - 79
D = 60 - 69
F = 0 - 59
"""

grade = 79

if 90 <= grade <= 100:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
elif 0 <= grade < 60:
    print("F")
