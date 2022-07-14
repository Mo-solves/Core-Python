the_simpsons = ["Home", 'Marge', 'Bart', 'Lisa', 'Maggie']

# print(the_simpsons[::-1])
for char in the_simpsons[::-1]:
    print(f'{char} has a total of {len(char)} characters.')

print(reversed(the_simpsons))
print(type(reversed(the_simpsons)))

for char in reversed(the_simpsons):
    print(f'{char} has a total of {len(char)} characters.')
