# Define a long_word function that accepts a string
# The function should return a Boolean that refects
# whether the string has more than 7 characters

def long_word(word):
    return len(word) > 7


print(long_word("mohamed"))
print(long_word("magnificent"))
print()
# Define a first_longer_than_second function that accepts two string arguments.
# The function should return a True if the first string is longer than the second
# and False otherwise (including if they are equal in length)


def first_longer_than_second(word1, word2):
    return len(word1) > len(word2)


print(first_longer_than_second("Python", "Ruby"))
print(first_longer_than_second('cat', 'mouse'))
print(first_longer_than_second('Steven', 'Seagal'))
