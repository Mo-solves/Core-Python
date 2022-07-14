employee = ('Mohamed', 'Abdi', 'Programmer', 25)

first_name, last_name, *details = employee
print(first_name)
print(last_name)
print(details)

*names, position, age = employee
print(names)
print(position)
print(age)

first_name, *details, age = employee
print(first_name)
print(details)
print(age)

first_name, last_name, position, *details = employee
print(details)
