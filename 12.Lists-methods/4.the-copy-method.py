units = ['Meter', 'Kilogram', 'Second', 'Ampere', 'Kelvin', 'Candela', 'Mole']

more_units = units.copy()

print(units)
print(more_units)

units.remove('Meter')
print(units)
print(more_units)

# copy a list
even_more_units = units[:]
print(even_more_units)

units.remove('Second')
print(units)
print(even_more_units)
