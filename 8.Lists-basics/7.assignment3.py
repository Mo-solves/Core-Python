# Define a split_in_two function that accepts a list and a number
# If the number is even, return the list elements from the third element
# to the end of the list
#
# If the number is odd, return the list element from index 0 (inclusive) to 2 (exclusive)

def split_in_two(value, number):
    if number % 2 == 0:
        return value[2:]
    return value[0:2]


values = ['a', 'b', 'c', 'd', 'e', 'f']

print(split_in_two(values, 3))
print(split_in_two(values, 4))
print(split_in_two(values, 1))
print(split_in_two(values, 10))
