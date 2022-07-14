numbers = [4, 7, 2, 9]
print(sorted(numbers))
print(numbers)

salaries = {
    'Executive Assistant': 20,
    'CEO': 100
}

print(sorted(salaries))
print(salaries)

wheel_count = {
    'truck': 2,
    'car': 4,
    'bus': 8
}

print(sorted(wheel_count.items()))

for vehicle, count in sorted(wheel_count.items()):
    print(f'the next vehicle is a {vehicle} and it has {count} wheels')
