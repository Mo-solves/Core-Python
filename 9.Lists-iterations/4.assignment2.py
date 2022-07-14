# Define a smallest_number function that accepts a list of numbers
# It should return the smallest value in the list
#

def smallest_number(numbers):
    smallest = numbers[0]
    for number in numbers:
        if smallest > number:
            smallest = number
    return smallest


print(smallest_number([1, 2, 3]))
print(smallest_number([3, 2, 1]))
print(smallest_number([4, 5, 4]))
print(smallest_number([-3, -2, -1]))

print()

# Define a concatenate function that accepts a list of strings
#
# The function should return a concatenated string which consists of
# all list elements whose length is greater than 2 characters


def concatenate(lists):
    total = ''
    for list in lists:
        if len(list) > 2:
            total += list
    return total


print(concatenate(['abc', 'def', 'ghi']))
print(concatenate(['abc', 'de', 'fgh', 'ic']))
print(concatenate(['ab', 'cd', 'ef', 'gh']))

print()

# Define a super_sum function that accepts a list of strings
# The function should sum the index positions of the first occurence of the letter "s" in each
#
# Not every word is guaranteed to have an "s"
# Don't use "sum" as a variable name as it's a build-in keyword


def super_sum(lists):
    total = 0
    for list in lists:
        index = list.index('s')
        total += index
    return total


print(super_sum([]))
print(super_sum(['mustache']))
print(super_sum(['mustache', 'greatest']))
print(super_sum(['mustache', 'pessimist']))
print(super_sum(['mustache', 'greatest', 'almost']))


# super_sum([])
# super_sum(['mustache'])
