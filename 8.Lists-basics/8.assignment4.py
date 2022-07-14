# Declare a nested_extraction function that accepts a list of lists and an index position
#
# The function should use the index as the basis of finding both the nested list and the element from that list with the given index position
#
# you can assume the number of lists will alwaus be equal to
# the number of elements within each of them

def nested_extraction(nl, index):
    return nl[index][index]


nl = [[3, 4, 5], [7, 8, 9], [10, 11, 12]]

print(nested_extraction(nl, 0))
print(nested_extraction(nl, 1))
print(nested_extraction(nl, 2))

print()

# Declare a beginning_and_end function that accepts a list of elements
#
# It should return True if the first and last elements in the list are equal and False if they are unequal
#
# Assume the list will always have at least 1 element


def beginning_and_end(number):
    return number[0] == number[-1]


print(beginning_and_end([1, 2, 3, 1]))
print(beginning_and_end([1, 2, 3, 4, 5]))
print(beginning_and_end(['a', 'b', 'a']))
print(beginning_and_end([15]))

print()

# Declare a long_word_in_collection function that accepts a list and a string
# The function should return True if
# - the word exists in the list AND
# - the word has more than 4 characters


def long_word_in_collection(list, word):
    if word in list and len(word) > 4:
        return True
    return False


words = ['cat', 'dog', 'rhino']

print(long_word_in_collection(words, 'rhino'))
print(long_word_in_collection(words, 'cat'))
print(long_word_in_collection(words, 'monkey'))
