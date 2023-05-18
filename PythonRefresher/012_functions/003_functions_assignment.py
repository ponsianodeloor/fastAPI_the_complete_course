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


#del * a la derecha son obligatorios los parametros
def make_dictionary(username, *, name, age):
    username_dictionary = {
        'username': username,
        'name': name,
        'age': age
    }
    return username_dictionary

user_params = {
    'username': 'xyz',
    'name': 'abc',
    'age': 10,
}

user_dict = make_dictionary('ponsianodeloor', name='Ponsiano De Loor', age='34')
print(user_dict)


#destructura de diccionario enviando el diccionario y no los parametros esperados
get_params = make_dictionary(**user_params)
print(user_dict)
