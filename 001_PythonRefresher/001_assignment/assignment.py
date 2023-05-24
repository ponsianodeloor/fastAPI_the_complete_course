"""
Tienes $50
compras un producto en $15
con un impuesto de 3%
imprimir cuanto dinero tienes
"""

my_money = 50

product = 15
tax_percent = 3


buy_product = (product + ((product * tax_percent) / 100))

print(my_money - buy_product)
