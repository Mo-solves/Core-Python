pizzaz = [
    'Mushroom',
    'Pepperoni',
    'Sausage',
    'Barbecue Chicken',
    'Pepperoni',
    'Sausage'
]

print(pizzaz.index('Barbecue Chicken'))
print(pizzaz.index('Pepperoni'))
print(pizzaz.index('Sausage'))

if 'Olives' in pizzaz:
    print(pizzaz.index('Olives'))

print(pizzaz.index('Pepperoni', 2))
print(pizzaz.index('Sausage', 3))
