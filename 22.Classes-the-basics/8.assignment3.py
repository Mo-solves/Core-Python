# Declare a Zombie class that accepts health and brains_eaten parameters

# In the initialization process for a Zombie object, assign the
# two parameters to two attributes with the same name

# If the instantiation does not pass a health parameter,
# it should be assigned default value of 100

# If the instantiation does not pass a brains_eaten parameter,
# it should be assigned a default value of 5

# Instantiate a Zombie object with 80 health and 5 brains eaten
# assign it to a "sally" variable

# Instantiate a Zombie object with 120 health and 3 brains eaten
# assign it to a "bob" variable

# Instantiate a Zombie object with no custom parameters
# assign it to a "benjamin" variable

# Practice instantiating the objects with both positional and keyword arguments

class Zombie():
    def __init__(self, health=100, brains_eaten=5):
        self.health = health
        self.brains_eaten = brains_eaten


sally = Zombie(80)
print(sally.health, sally.brains_eaten)

bob = Zombie(health=120, brains_eaten=3)
print(bob.health, bob.brains_eaten)

benjamin = Zombie()
print(benjamin.health, benjamin.brains_eaten)

sue = Zombie(brains_eaten=10)
print(sue.health, sue.brains_eaten)
