# Declare a negative_energy function that accepts a numeric argument
# and returns its absolute value
# The absolute value is the number's distance from zero

def negative_energy(number):
    if number > 0:
        return number
    elif number < 0:
        return -1 * number
    else:
        return number


print(negative_energy(5))
print(negative_energy(10))
print(negative_energy(-5))
print(negative_energy(-8))
print(negative_energy(0))
