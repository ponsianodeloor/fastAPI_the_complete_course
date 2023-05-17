"""
Call a function inside other function
"""


def buy_item(cost_of_item):
    return cost_of_item + add_tax_to_item(cost_of_item)


def add_tax_to_item(cost_of_item):
    iva_percent = 12
    return cost_of_item * (iva_percent / 100)


final_cost = buy_item(50)
print(final_cost)

