# Declare a common_elements function that accepts a dictionary
# It should return a list with all of the elements that are found
# as both a key and a value in the dictionary

my_dict = {
    'A': 'K',
    'B': 'D',
    'C': 'A',
    'D': 'Z'
}


def common_elements(my_dict):
    # common = []
    # for key in my_dict.keys():
    #     if key in my_dict.values():
    #         common.append(key)
    # return common
    return [key for key in my_dict.keys() if key in my_dict.values()]


print(common_elements(my_dict))
