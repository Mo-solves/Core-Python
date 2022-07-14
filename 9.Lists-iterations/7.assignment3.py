# Define an in_list function that accepts a list of strings and a separate string
# Return the index where the string exists in the list
# if the string does not exist, return -1
# Do NOT use the find or index methods

def in_list(strings, word):
    for idx, task in enumerate(strings):
        if word in task:
            return idx
    return -1


strings = ['enchanted', 'sparks fly', 'long live']

print(in_list(strings, 'enchanted'))
print(in_list(strings, 'sparks fly'))
print(in_list(strings, 'fifteen'))
print(in_list(strings, 'love story'))

print()

# Define a sum_of_values_and_indices function that accepts a list of numbers.
# It should return the sum of all of the elements along with their index value


def sum_of_values_and_indices(numbers):
    total = 0
    for idx, value in enumerate(numbers):
        total += idx + value
    return total


print(sum_of_values_and_indices([1, 2, 3]))
print(sum_of_values_and_indices([0, 0, 0, 0]))
print(sum_of_values_and_indices([]))
