# Create an empty list and assignt it to the variable "empty"

empty = []

# Create a list with a single Boolean - True - and assign it to the variable "active"

active = [True]

# Create a list with 5 integers of your choice and assign it to the variable "facorite_numbers"

favorite_numbers = [10, 21, 80, 15, 20]

# Create a list with 3 strings - "red", "green", "blue"
# and assign it to the variable "colors"

colors = ["red", 'green', 'blue']

# Declare an is_long function that accepts a single list as an argment
# It should return True if the list has more than 5 elements, and False otherwise


def is_long(list):
    return True if len(list) > 5 else False


print(is_long([1, 2, 3, 4]))
print(is_long([12, 1, 5, 4, 8, 9, 2, 15]))
