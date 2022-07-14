# Define a first_three_characters function that accepts a string argument
# The functiom should return the first 3 characters of the string

def first_three_characters(string):
    return string[:3]


print(first_three_characters('dynasty'))
print(first_three_characters('empire'))

# Define a last_five_characters function that accepts a string argument
# The function should return the last 5 characters of the string.


def last_five_characters(string):
    return string[-5:]


print(last_five_characters('dynasty'))
print(last_five_characters('empire'))

# Define a is_palindrome function that accepts a string argument
# The function should return True if the string is spelled
# the same backward as it is forwards
# return False otherwise


def is_palindrome(string):
    return string == string[::-1]


print(is_palindrome('racecar'))
print(is_palindrome('yummy'))
print(is_palindrome('mom'))
