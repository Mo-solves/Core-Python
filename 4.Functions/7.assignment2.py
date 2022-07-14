# Define a string_adder function that accepts two strings (a and b) as arguments
# It should return a concatenated version of the arguments with space in between.
# if the user does not pass in arguments, both arguments should default to an empty string

def string_adder(a='', b=''):
    return a + ' ' + b


print(string_adder('hello', 'world'))
print(string_adder('Emilio', 'Estevez'))
print(string_adder())
print(string_adder('Tiger'))

print()
# Define a multiplier function that accepts three integers as arguments
# Return the product of the arguments
# The product is the total when values are multiplied together
# If the user does not provide any arguments, all three parameters
# should have default argument of 1.


def multiplier(a=1, b=1, c=1):
    return a * b * c


print(multiplier(2, 2, 2))
print(multiplier())
print(multiplier(3))
print(multiplier(2, 5))
