# Define a first_and_last function that accepts a list of strings
# The function should return a concatenation of the first element and the last element
# Assume the list will always have 1 or more elements

def first_and_last(string):
    return string[0] + string[-1]


print(first_and_last(['a', 'b', 'c']))
print(first_and_last(['bob', 'tom', 'rob']))
print(first_and_last(['a']))

print()

# Define a product_of_even_indices function that accepts a list of numbers
# The list will always have 6 total elements
# The function should return the product (multiplied total)
# of all numbers at an even index (0, 2, 4)


def product_of_even_indices(number):
    start_index = 0
    multiplied_events = 1

    while start_index < len(number) - 1:
        if start_index % 2 == 0:
            multiplied_events *= number[start_index]
        start_index += 1

    return multiplied_events


print(product_of_even_indices([1, 2, 3, 4, 5, 6]))
print(product_of_even_indices([3, 4, 3, 5, 3, 6]))

print(product_of_even_indices([2, 5, 8, 9]))

print()

# Define a first_letter_of_last_string function that accepts a list of strings
# It should return one character - the first letter of the last string in the list
# Assume the list will always have at least one string


def first_letter_of_last_string(string):
    return string[-1][0]


print(first_letter_of_last_string(['cat', 'dog', 'zebra']))

print(first_letter_of_last_string(['nonsense']))
