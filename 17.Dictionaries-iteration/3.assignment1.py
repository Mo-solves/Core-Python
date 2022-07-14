# Declare an invert function that accepts a dictionary object
# The function should return a new dictionary where the
# keys and values from the original dictionary are inverted
# Each key should now be a value, and each value should be a key
# Assume both the keys and values of the dictionary are immutable

my_dict = {
    'A': 'B',
    'C': 'D',
    'E': 'F'
}


def invert(my_dict):
    revert_dic = {}
    for key, value in my_dict.items():
        revert_dic[value] = key
    return revert_dic


print(invert(my_dict))

# Declare a count_of_value function that accepts a dictionary and an integer
# It should return a count of number of times the integer appears
# as a value among the dictionary's value

my_dict2 = {'a': 5, 'b': 3, 'c': 5}


def count_of_value(my_dict, number):
    counter = 0
    for _, value in my_dict.items():
        if value == number:
            counter += 1
    return counter


print(count_of_value(my_dict2, 5))
print(count_of_value(my_dict2, 3))
print(count_of_value(my_dict2, 2))

# Declare a sum_of_values that accepts a dictionary and a list of strings
# The dictionary will have keys of strings and values of numbers
#
# The function should return the sum of values for a dictionary

my_dict3 = {'a': 5, 'b': 3, 'c': 10}


def sum_of_values(my_dict, lists):
    total = 0
    for key, value in my_dict.items():
        if key in lists:
            total += value
    return total


print(sum_of_values(my_dict3, ['a']))
print(sum_of_values(my_dict3, ['a', 'c']))
print(sum_of_values(my_dict3, ['a', 'c', 'b']))
print(sum_of_values(my_dict3, ['z']))
