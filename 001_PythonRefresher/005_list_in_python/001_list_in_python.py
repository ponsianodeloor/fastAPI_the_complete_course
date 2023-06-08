

my_list = [80, 96, 72, 100, 8]
print(my_list)
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[4])
# print(my_list[5]) error

print("Ordenar los elementos de la lista")
my_list.sort()
print(my_list)

people_list = ["Ponsiano", "Thomas"]

print(people_list)
print(people_list[-1])
people_list[0] = "PonWick"
print(people_list)
elements = len(people_list)
print(f"Elementos en la lista people_list: {elements}")

print(people_list[0:2])

#agregar un elemento a la lista con append

people_list.append("De Loor")
print("Se agrega un elemento a la lista")
print(people_list)

people_list.insert(2, "BabaYaga")
print("Se inserta un elemento en la lista")
print(people_list)

people_list.remove("De Loor")
print("Se elimina un elemento a la lista ingresando el valor")
print(people_list)

people_list.pop(0)
print("Se elimina un elemento a la lista ingresando el indice")
print(people_list)
print(len(people_list))

