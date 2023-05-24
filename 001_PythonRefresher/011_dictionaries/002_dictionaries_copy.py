"""
Dictionaries
"""


user_dictionary = {
    'username': 'ponsianodeloor',
    'name': 'Ponsiano De Loor',
    'age': '35'
}

user_dictionary_2 = user_dictionary
#user_dictionary_2 = user_dictionary.copy()

user_dictionary_2.pop('age')

print(user_dictionary)
print(user_dictionary_2)

for x, y in user_dictionary.items():
    print(f"k {x} v {y}")

for x, y in user_dictionary_2.items():
    print(f"k {x} v {y}")

