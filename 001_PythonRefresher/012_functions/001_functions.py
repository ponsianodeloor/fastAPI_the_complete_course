"""
Functions
"""


print("Hello and welcome to the functions")


def my_function():
    print("Print inside my function")


def print_my_name(name):
    print(f"Hello {name}")


def print_name_and_lastname(name, lastname):
    print(f"Hello {name} {lastname}")


def print_color():
    color = "Blue"
    print(color)


my_function()
print_my_name('Ponsiano')
print_name_and_lastname('Ponsiano', 'De Loor')
color = "Red"
print(color)
print_color()


print("Se puede asignar la variable sin importar el orden siempre y cuando se indique la propiedad")


def print_numbers(highest_numbers, lowest_numbers):
    print(highest_numbers)
    print(lowest_numbers)


print_numbers(lowest_numbers=3, highest_numbers=10)


def multiply_numbers(a, b):
    return a * b


solution = multiply_numbers(4, 5)
print(solution)


def print_list(list_of_numbers):
    for x in list_of_numbers:
        print(x)


number_list = [1, 2, 3, 4, 5, 6]

print_list(number_list)

