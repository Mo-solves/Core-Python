# Define a Clothing superclass with wear and sell instance methods
# the wear method should return the string "I'm wearing this fashionable piece of clothing!"
# The sell method should return the string "Buy my piece of clothing"

# Define a Socks subclass that inherites from Clothing superclass
# it should define a lose_one instance method that
# returns the string "Where did my other one go?"
# it should overrite the wear method to
# return the string "Take a look at my socks! They're gorgeous"
# it should override the sell method to
# return the string "Buy my socks!"

class Clothing():
    def wear(self):
        return "I'm wearing this fashionable piece of clothing!"

    def sell(self):
        return "Buy my piece of clothing"


class Socks(Clothing):
    def lose_one(self):
        return "Where did my other one go?"

    def wear(self):
        return "Take a look at my socks! They're gorgeous"

    def sell(self):
        return "Buy my socks!"


clean_socks = Socks()
print(clean_socks.wear())
print(clean_socks.lose_one())
