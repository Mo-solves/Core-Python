pokemon = {
    'Fire': ['Charmander', 'Charmeleon', 'Charizard'],
    'Water': ['Squirtle', 'Warturtle', 'Blastoise'],
    'Grass': ['Bulbasaur', 'Venusaur', 'Ivysaur']
}

print('Fire' in pokemon)
print('Grass' in pokemon)
print('Electric' in pokemon)
print('fire' in pokemon)

print('Electric' not in pokemon)
print('fire' not in pokemon)
print('Zombie' not in pokemon)
print('Water' not in pokemon)

if 'Zombie' in pokemon:
    print(pokemon['Zombie'])
else:
    print('The category of Zombie does not exist!')
