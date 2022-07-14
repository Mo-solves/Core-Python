# Define a Chocolate class that accepts and assigns a cacao_content

# Define a "sweet" class method that returns a
# Chocolate object with a cacao_content value of 30

# Define a "semisweet" class method that returns a
# Chocolate object with a cacao_content value of 50

# Define a "bittersweet" class method that returns a
# Chocolate object with a cacao_content value of 70

# Define a "bitter" class method that returns a
# Chocolate object with a cacao_content value of 99
class Chocolate():
    def __init__(self, cacao_content):
        self.cacao_content = cacao_content

    @classmethod
    def sweet(cls):
        return cls(30)

    @classmethod
    def semisweet(cls):
        return cls(50)

    @classmethod
    def bittersweet(cls):
        return cls(70)

    @classmethod
    def bitter(cls):
        return cls(99)


sweet = Chocolate.sweet()
print(sweet.cacao_content)

semisweet = Chocolate.semisweet()
print(semisweet.cacao_content)

bittersweet = Chocolate.bittersweet()
print(bittersweet.cacao_content)

bitter = Chocolate.bitter()
print(bitter.cacao_content)
