# Declare a right_words function that accepts a list of words and a number
# Return a new list with the words that have a length equal to the number

def rigth_words(words, number):
    return list(filter(lambda word: len(word) == number, words))


print(rigth_words(['cat', 'dog', 'bean', 'ace', 'heart'], 3))
print(rigth_words(['cat', 'dog', 'bean', 'ace', 'heart'], 5))
print(rigth_words([], 4))

print()
# Declare an only_odds function
# It should accept a list of whole numbers
# It should return a list with only the odd numbers from the original list


def only_odds(numbers):
    return list(filter(lambda number: number % 2 != 0, numbers))


print(only_odds([1, 3, 5, 6, 7, 8]))
print(only_odds([2, 4, 6, 8]))
print()

# Declare a count_of_a function that accepts a list of strings
# It should return a list with counts of how many 'a' characters appear per string


def count_of_a(words):
    return list(map(lambda word: word.count('a'), words))


print(count_of_a(['alligator', 'aardvark', 'albatross']))
print(count_of_a(['plywood']))
print(count_of_a([]))
