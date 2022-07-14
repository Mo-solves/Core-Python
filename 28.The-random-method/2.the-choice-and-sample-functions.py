import random

print(random.choice(['Bob', 'Moe', 'Curly']))
print(random.choice((1, 2, 3)))
print(random.choice('elephant'))

lotter_numbers = [random.randint(1, 50) for value in range(51)]
# print(lotter_numbers)

print(random.sample(lotter_numbers, 1))
print(random.sample(lotter_numbers, 2))
print(random.sample(lotter_numbers, 6))
