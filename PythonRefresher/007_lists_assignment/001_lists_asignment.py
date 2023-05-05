zoo = ['tiger', 'bear', 'monkey', 'lion', 'penguin']

print("List of animals from zoo")
print(zoo)

print("Delete the animal at the 3rd index")
zoo.pop(3)
print(zoo)

print("Append a new animal at the end of the list")
zoo.append("Gorilla")
print(zoo)

print("Delete the animal at beginning of the list")
zoo.pop(0)

print("Print all the animals")
print(zoo)

for x in zoo:
    print(x)

print("Print only the first 3 animals")
print(zoo[0:3])


