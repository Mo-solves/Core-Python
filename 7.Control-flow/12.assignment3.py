# Define a divisible_by_three_and_four function that accepts a number as its argument
# It should return True if the number is evenly divisible by both 3 and 4
# It should return false otherwise

def divisible_by_three_and_four(number):
    if number % 3 == 0 and number % 4 == 0:
        return True
    return False


print(divisible_by_three_and_four(3))
print(divisible_by_three_and_four(4))
print(divisible_by_three_and_four(12))
print(divisible_by_three_and_four(18))
print(divisible_by_three_and_four(24))

print()
# Declare a string_theory function that accepts a string as an argument
# It should return True if the string has more than 3 characters
# and starts with a capital "S". it should return False otherwise


def string_theory(string):
    if string.startswith('S') and len(string) > 3:
        return True
    return False


print(string_theory('Sansa'))
print(string_theory('Story'))
print(string_theory('See'))
print(string_theory('Fable'))
