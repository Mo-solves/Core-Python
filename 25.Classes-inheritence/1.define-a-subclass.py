class Store():
    def __init__(self):
        self.owner = 'Mohamed'

    def exclaim(self):
        return 'Lots of stuff to buy, come inside!'


class CoffeShop(Store):
    pass


starbucks = CoffeShop()

print(starbucks.owner)
print(starbucks.exclaim())
