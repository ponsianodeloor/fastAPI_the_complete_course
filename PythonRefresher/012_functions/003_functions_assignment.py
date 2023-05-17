"""
Create a function than receive 3 parameters an return a dictionary
"""


def make_dictionary(username, name, age):
    username_dictionary = {
        'username': username,
        'name': name,
        'age': age
    }
    return username_dictionary


user_dict = make_dictionary(username='ponsianodeloor', name='Ponsiano De Loor', age='34')
print(user_dict)