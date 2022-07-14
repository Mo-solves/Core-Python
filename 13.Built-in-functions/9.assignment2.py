# Declare a greater_sum function that accepts two lists of numbers
# It should return the list with the greatest sum
# You can assume the lists will always have different sums

def greater_sum(first, second):
    return first if sum(first) > sum(second) else second


print(greater_sum([1, 2, 3], [1, 2, 4]))
print(greater_sum([4, 5], [2, 3, 6]))
print(greater_sum([1], []))

print()
# Declare a sum_diffetence function that accepts two lists of numbers
# It should return the difference between the sum of values in the first list and the second list


def sum_difference(first, second):
    return sum(first) - sum(second)


print(sum_difference([1, 2, 3], [1, 2, 4]))
print(sum_difference([4, 5], [2, 3, 6]))
print(sum_difference([1], []))
