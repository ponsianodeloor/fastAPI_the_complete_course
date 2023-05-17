"""
Standard library comes with Python

Useful methods!
"""

# Random
import random, math

types_of_drinks = ['Soda', 'Coffee', 'Water', 'Tea']
print(random.choice(types_of_drinks))


number_between_one_and_ten = random.randint(1, 10)
print(number_between_one_and_ten)

square_number = number_between_one_and_ten * number_between_one_and_ten
print(square_number)
square_root = math.sqrt(square_number)
print(square_root)
