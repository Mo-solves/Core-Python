# immutable objects
a = 3
b = a

a = 5
print(a)
print(b)

# mutable objects
a = [1, 2, 3]
b = a

a.append(4)
print(a)
print(b)

b.append(5)
print(a)
print(b)
