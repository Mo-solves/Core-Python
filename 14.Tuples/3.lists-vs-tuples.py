birthday = (11, 9, 1998)

print(len(birthday))

print(birthday[0])
print(birthday[1])
print(birthday[2])


print(birthday[-1])
print(birthday[-2])
print(birthday[-3])

# Difference between lists and tuples
# Tuples are unmutable

# birthday[1] = 13

addresses = (
    ['Hudson Street', 'New York', 'NY'],
    ['Franklin Street', 'San Francisco', 'CA']
)

addresses[1][0] = "Polk Street"
# print(addresses)

print(dir(birthday))
