from datetime import date

"""
User input
"""


user = input("Ingrese su nombre: ")
date_birthday = input("Ingrese su fecha de nacimiento en el siguiente formato dd/mm/yyyy: ")

day = int(date_birthday[0:2])
month = int(date_birthday[3:5])
year = int(date_birthday[6:10])

future_birthday = date(date.today().year, month, day)
today = date.today()

remaining_birthday_days = (future_birthday - today).days
age = round((today - date(year, month, day)).days / 365)

print(f"Hola {user}, tu fecha de nacimiento es {date_birthday} y cumples {age} anos en {remaining_birthday_days} dias ")
