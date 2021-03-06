# Declare a delete_all function that accepts a list of strings and a target string
# Remove all occurrences of the target string from the list and return it

def delete_all(lists, string):
    # for list in lists:
    #     if list == string:
    #         lists.remove(list)
    # if string in lists:
    #     lists.clear()
    while string in lists:
        lists.remove(string)
    return lists


print(delete_all([1, 3, 5], 3))
print(delete_all([5, 3, 5], 5))
print(delete_all([4, 4, 4], 4))
print(delete_all([4, 4, 4], 6))

print()
# Declare a push_or_pop function that accepts a list of numbers
# Build up and return a new list by iterating over the list of numbers
# IF a number is greater than 5, add it to the end of the new list
# If a number is less than or equal to 5, remove the last element added to the new list
# Assume the order of numbers in the argument will never require removing from an empty list


def push_or_pop(numbers):
    new_list = []
    for number in numbers:
        if number > 5:
            new_list.append(number)
        elif number <= 5 and len(numbers) > 0:
            new_list.pop()
    return new_list


print(push_or_pop([10]))
print(push_or_pop([10, 4]))
print(push_or_pop([10, 20, 30]))
print(push_or_pop([10, 20, 2, 30]))
