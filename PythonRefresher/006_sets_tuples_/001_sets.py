my_set = {1, 2, 3, 4, 5, 1, 2}
print(my_set)
print(len(my_set))

print("Mostrar los elementos de un diccionario en un for in")
for x in my_set:
    print(x)

#print(my_set[0]) #no se pueden mostrar los elementos de un diccionario como en una lista
my_list = list(my_set)
print(my_list[0:4])

my_set.discard(3)
print(my_set)

my_set.add(6)
my_set.update([7, 8])
my_set.clear()
print(my_set)



