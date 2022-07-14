# Par A: Instantiation

# Define a BusTrip class that is initialized with a destination,
# a bus company, and a price for the trip
# preserve the arguments as attrubutes on the object
# The choice of whether to use protected attribute is up to u

# Part B: String Representation

# The string representation of a BusTrip object must be a string in the form of:
# "You paid 24.99 to Greyhound to go to Boston"
# In this example, "Boston" is the destination, "Greyhouse" is the bus company, and 24.99 is the price
# These are all fed in as arguments when a BusTrip object is initialized

# Part C: Equalty

# Implement equality logic between two different BusTrip objects
# Two BusTrips object considered equal if:
# -- they have the same destination
# -- their price is within 3 dollars of each other
# Hint: use Python's abs function to calculate the absolute value of a num

class BusTrip():
    def __init__(self, destination, company, price):
        self._destination = destination
        self.company = company
        self.price = price

    @property
    def destination(self):
        return self._destination

    def __str__(self):
        return f'You paid {self.price} to {self.company} to go to {self._destination}'

    def __eq__(self, other_trip):
        same_destination = self.destination == other_trip.destination
        insignificant_price_difference = abs(
            self.price - other_trip.price) <= 3
        return same_destination and insignificant_price_difference


boston1 = BusTrip(destination='Boston', company='Greyhound', price=24.99)
boston2 = BusTrip(destination='Boston', company='Megabus', price=22.99)
boston3 = BusTrip(destination='Boston', company='Megabus', price=49.99)
philly = BusTrip(destination='Philadelphia', company='Peter Pan', price=12.99)

print(boston1)
print(boston2)
print(boston1 == philly)
print(boston1 == boston2)
print(boston1 == boston3)
