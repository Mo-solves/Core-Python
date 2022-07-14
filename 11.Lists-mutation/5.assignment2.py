# Declare a length_match function that accepts a list of strings and an integer
# It should return a count of the number of strings whose length is equal to the number

def length_match(lists, number):
    counter = 0
    for list in lists:
        if len(list) == number:
            counter += 1
    return counter


print(length_match(['cat', 'dog', 'kangaroo', 'mouse'], 3))
print(length_match(['cat', 'dog', 'kangaroo', 'mouse'], 5))
print(length_match(['cat', 'dog', 'kangaroo', 'mouse'], 4))
print(length_match([], 5))
print(length_match(['cat', 'dog', 'kangaroo', 'mouse'], 8))

print()

# Declare a sum_from function that accepts two numbers as arguments.
# The second number will always be greater than the first number
# The function should return the sum of all numbers from the
# first number to the second number


def sum_from(start, end):
    sum = 0
    # while start <= end:
    #     sum += start
    #     start += 1
    for number in range(start, end + 1):
        sum += number
    return sum


print(sum_from(1, 2))
print(sum_from(1, 5))
print(sum_from(3, 8))
print(sum_from(9, 12))

print()
# Declare a same_index_values function that accepts two lists
# The function should return a list of the index positions in which the lists have equal elements


def same_index_values(lists1, lists2):
    same_index = []
    for idx, value in enumerate(lists1):
        # if lists1[idx] == lists2[idx]:
        if value == lists2[idx]:
            same_index.append(idx)
    return same_index


print(same_index_values([1, 2, 3], [3, 2, 1]))
print(same_index_values(['a', 'b', 'c', 'd'], ['c', 'b', 'a', 'd']))
