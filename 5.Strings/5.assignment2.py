# Define a same_first_and_last_letter function that accepts a string as an argument.
# The function should return True if the first and last character are equal,
# and False otherwise
# Assume the string will always have 1 or more characters.

def same_first_and_last_letter(word):
    return word[0] == word[-1]


print(same_first_and_last_letter('runner'))
print(same_first_and_last_letter('Runner'))
print(same_first_and_last_letter('clock'))
print(same_first_and_last_letter('q'))

print()

# Define a three_number_sum function that accepts a 3-character string as an argument
# The function should add up the sum of the digits of the string


def three_number_sum(string):
    return int(string[0]) + int(string[1]) + int(string[2])


print(three_number_sum('123'))
print(three_number_sum('567'))
print(three_number_sum('444'))
print(three_number_sum('000'))
