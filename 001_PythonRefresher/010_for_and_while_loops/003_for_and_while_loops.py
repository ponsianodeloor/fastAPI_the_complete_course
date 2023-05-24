"""
For & While Loops
"""

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
    if i == 4:
        break
else:
    print("i es ahora mayor o igual a 5")


