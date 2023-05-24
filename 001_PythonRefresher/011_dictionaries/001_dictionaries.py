"""
Dictionaries
"""


user_dictionary = {
    'username': 'ponsianodeloor',
    'name': 'Ponsiano De Loor',
    'age': '35'
}

print(user_dictionary)
print(user_dictionary.get('username'))

user_dictionary['married'] = True
print(user_dictionary)
print(user_dictionary.get('married'))

print("Tamaño de elementos del diccionario")
print(len(user_dictionary))

print("Remover elemento del diccionario con pop")
print(len(user_dictionary))

#user_dictionary.clear()
#print(user_dictionary)

#del user_dictionary
#print(user_dictionary)

print("Al usar un for en el diccionario solo imprime las llaves")

for x in user_dictionary:
    print(x)

print("Imprimir llave y valor")
for x, y in user_dictionary.items():
    print(f"Llave {x} valor {y}")