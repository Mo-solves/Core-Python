# Declare a Musician class that accepts a name argument in its initialization
# The initialization should assign a name argument to a name attribute
# In addition, each Musician object should have a albums attribute
# that begins as an empty list
# Define a release_album instance method on a Musician that accepts a title (string)
# It should append the string to the end of the list held by the
# albums attribute

# Declare a Drummer subclass that inhirits from the Musician superclass
# In addition to a name, a drummer should also have a stamina attribute
# represented by an integer
# The subclass should invoke the Musician superclass's initialization
# procedure and pass it the drummer's name
# It should also set the stamina attribute in its own initialization process

class Musician():
    def __init__(self, name):
        self.name = name
        self.albums = []

    def release_album(self, title):
        return self.albums.append(title)


class Drummer(Musician):
    def __init__(self, name, stamina):
        super().__init__(name)
        self.stamina = stamina


lars = Drummer(name='Lars', stamina=2)
print(lars.name)
print(lars.stamina)
print(lars.albums)

lars.release_album('Ride the lightning')
print(lars.albums)

lars.release_album('Master of Puppets')
print(lars.albums)
