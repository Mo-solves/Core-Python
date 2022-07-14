print(set([1, 2, 3]))
print(set([1, 2, 3, 3, 2, 1]))

print(set((1, 2)))
print(set((1, 2, 1, 2, 1)))

print(set('abc'))
print(set('aabbcc'))

print(set({'key': 'value'}))

pholisophers = ['Plato', 'Socrates', 'Aristotle',
                'Pythagoras', 'Socrates', 'Plato']
pholisophers_set = set(pholisophers)
pholisophers = list(pholisophers_set)
print(pholisophers)
