# Define a sum_of_lengths function that accepts a list of strings
# The function should return the sum of the string lengths

def sum_of_lengths(lists):
    total_length = 0
    for list in lists:
        total_length += len(list)

    return total_length


print(sum_of_lengths(['Hello', 'Bob']))
print(sum_of_lengths(['Nonsense']))
print(sum_of_lengths(['Nonsense', 'or', 'confidence']))

print()
# Define a product function that accepts a list of numbers
# The function should returm the product of numbers
# The list will always have at least one value


def product(numbers):
    multiply = 1
    for number in numbers:
        multiply *= number

    return multiply


print(product([1, 2, 3]))
print(product([4, 5, 6, 7]))
print(product([10]))
