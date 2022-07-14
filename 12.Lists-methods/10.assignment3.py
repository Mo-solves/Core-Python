# Define a nested_sum function that accepts a list of lists of numbers
# The function should return the sum of the values
# The list may contain empty lists

def nested_sum(lists):
    sum = 0
    for numbers in lists:
        for number in numbers:
            sum += number
    return sum


print(nested_sum([[1, 2, 3], [4, 5]]))
print(nested_sum([[1, 2, 3], [], [], [4], [5]]))
print(nested_sum([[]]))

print()
# Define a fancy_concatenate function that accepts a list of lists of string
# The function should return concatenated string
# The string in a list should only be concatenated if the length of the list is 3


def fancy_concatenate(string):
    concatenated = ''
    for lists in string:
        for list in lists:
            if len(lists) == 3:
                concatenated += list
    return concatenated


print(fancy_concatenate([['A', 'B', 'C']]))
print(fancy_concatenate([['A', 'B', 'C'], ['D', 'E', 'F']]))
print(fancy_concatenate([['A', 'B', 'C'], ['D', 'E', 'F', 'G']]))
print(fancy_concatenate([['A', 'B', 'C'], ['D', 'E']]))
print(fancy_concatenate([['A', 'B'], ['C', 'D']]))
