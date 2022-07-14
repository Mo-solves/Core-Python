# lambda functions are nameless functions
metals = ['Gold', 'silver', 'platinum', 'palladium']

print(list(filter(lambda metal: len(metal) > 5, metals)))

print(list(filter(lambda metal: 'p' in metal, metals)))

print(list(map(lambda word: word.count('l'), metals)))

print(list(map(lambda word: word.replace('s', '$'), metals)))
