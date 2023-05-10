"""
Given the variable my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
- Create a while loop that prints all elements of the my_list variable 3 times.
- When printing the elements use a for loop to print the elements
- However, if the element of the for loop is equal to Monday, continue without printing
"""

my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

i = 0
while i < 3:
    for x in my_list:
        if x == "Monday":
            print("------")
            continue
        print(x)
    i += 1
else:
    print("el valor de i es igual o mayor que 3")
