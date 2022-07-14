# Define a even_or_add function that accepts a single integer
# If the integer is even, the function should return the string "even"
# If the integer is odd, the function should return the string "odd"

def even_or_odd(number):
    if number % 2 == 0:
        return 'even'

    return 'odd'


print(even_or_odd(2))
print(even_or_odd(0))
print(even_or_odd(13))
print(even_or_odd(9))

print()
# Define a truthy_or_falsy function that accepts a single argument
# The function should return a string that reads "The value___is___"
# where the second space is the argument and the second space is
# either 'truthy' or 'falsy'


def truthy_or_falsy(input):
    if input:
        return(f'The value {input} is truthy')

    return(f'The value {input} is falsy')


print(truthy_or_falsy(0))
print(truthy_or_falsy(5))
print(truthy_or_falsy('Hello'))
print(truthy_or_falsy(''))
