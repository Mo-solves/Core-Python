numbers = [3, 4, 5, 6, 7]
# squares = []

# for number in numbers:
#     squares.append(number ** 2)

# print(squares)
# print(number)

# list comprehension
squares = [number ** 2 for number in numbers]
print(squares)
# print(number)

rivers = ['Amazon', 'Nile', 'Yangtze']
lengths = [len(river) for river in rivers]
print(lengths)

expressions = ['lol', 'rofl', 'lmao']
print([expression.upper() for expression in expressions])

decimals = [4.95, 3.28, 1.08]
print([int(decimal) for decimal in decimals])
