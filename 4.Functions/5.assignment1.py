# Define a easy_money function that accepts no parameters
# and always return the value of 100
def easy_money():
    return 100

# Define a best_food_ever function that accepts
# no parameters and always returns the string "Sushi"


def best_food_ever():
    return 'Sushi'

# Define a convert_to_currency function that accepts a single parameter (an integer)
# The function should conver the argument to a string
# Prefix it with a dollar sign, and return the result


def convert_to_currency(number):
    result = str(number)
    return '$' + result


result = convert_to_currency(8)
print(result)

result = convert_to_currency(15)
print(result)
