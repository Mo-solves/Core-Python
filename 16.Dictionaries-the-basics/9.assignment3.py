# Declare a delete_keys function that accepts two arguments:
# a dictionary and a list of strings
# For each string in the list, if the string exists as a dictionary key,
# Delete they key-value pair from the dictionary

# If the string does not exist as a dictionary key, avoid error
# The return value should be the modified dictionary object
my_dict = {
    'A': 1,
    'B': 2,
    'C': 3
}

strings = ['A', 'C']


def delete_keys(dictionary, lists):
    for list in lists:
        if list in dictionary:
            dictionary.pop(list)
    return dictionary


print(delete_keys(my_dict, strings))
