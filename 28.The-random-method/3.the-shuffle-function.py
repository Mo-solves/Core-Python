import random
import copy

characters = ['Warrior', 'Druid', 'Hunter', 'Rogue', 'Mage']

clone = characters[:]
clone = characters.copy()
clone = copy.copy(characters)

print(random.shuffle(clone))
print(characters)
print(clone)
