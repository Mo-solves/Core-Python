# Define a word_lengths function that accepts a string
# It should return a list with the lengths of each word

def word_lengths(sentence):
    words = sentence.split(' ')
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths


print(word_lengths('Mary Poppins was a nanny'))
print(word_lengths('Somebody stole my donut'))

print()

# Define a cleanup function that accepts a list of strings.
# The function should return the strings joined together by a space
# There's one BIG problem -- some of the strings are empty or only consist of space!
# These should NOT be included in the final string


def cleanup(lists):
    cleanup = []
    for list in lists:
        if list != ' ' and list != '':
            cleanup.append(list)
    result = ' '.join(cleanup)
    return result


print(cleanup(['cat', 'er', 'pillar']))
print(cleanup(['cat', ' ', 'er', '', 'pillar']))
print(cleanup(['', '', ' ']))
