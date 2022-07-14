# Declare a Musical class that accepts a name parameter
# In the initialization process for an object, assign the
# name parameter to a name attribute on the object
#


class Musical():
    def __init__(self, name):
        self.name = name


# Instantiate a Musical object with the name "Rent"
# and assign it to an "rent" variable
rent = Musical('Rent')
print(rent.name)

# Instantiate a Musical object with the name "Book of Mormon"
# and assign it to an "mormon" variabl
mormon = Musical('Book of Mormon')
print(mormon.name)

# Instantiate a Musical object with the name "Chicago"
# and assign it to an "chicago" variabl
chicago = Musical('Chicago')
print(chicago.name)

# Declare a Shape class that accepts a sides parameter

# In the initialization process for an object, assign the
# sides parameter to a sides attribute on the object


class Shape():
    def __init__(self, sides):
        self.sides = sides


# Instantiate a Shape object with 3 sides and assign it to a "triangle"var
triangle = Shape(3)
print(triangle.sides)

# Instantiare a Shape object with 4 sides and assign it to a "square" var
square = Shape(4)
print(square.sides)

# Instantiate a Shape object with 10 sides and assign it to a "decagon"var
decagon = Shape(10)
print(decagon.sides)

# Declare a Skycraper class that accepts name and year parameters

# In the initialization process for an object, assign the name parameter
# to a name attribute and the year parameter to a year attribute

# Instantiate a Skycrapper object with the name "Empire State Building"
# and the year 1931, assign it to a "empire" variable

# Instantiate a Skycrapper object with the name "One World Trade Center"
# and the year 2014, assign it to a "wtc" variable


class Skycrapper():
    def __init__(self, name, year):
        self.name = name
        self.year = year


empire = Skycrapper('Empire State building', 1931)
wtc = Skycrapper(name='One World Trade Center', year=2014)

print(empire.name, empire.year)
print(wtc.name, wtc.year)
