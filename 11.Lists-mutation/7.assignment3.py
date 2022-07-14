# Define an only_evens function that accepts a list of numbers
# It should return a new list consisting of only the even numbers from the original list

def only_evens(numbers):
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens

print(only_evens([4, 8, 15, 16, 23, 42]))
print(only_evens([1, 3, 5]))
print(only_evens([]))
print()

# Define a long_strings function that accepts a list of strings
# It should return a new list consisting of only the 
# strings that have 5 characters or more

def long_strings(strings):
    long_strings = []
    for string in strings:
        if len(string) >= 5:
            long_strings.append(string)
    return long_strings

print(long_strings(['Hello', 'Goodbye', 'Sam']))
print(long_strings(['Ace', 'Cat', 'Job']))
print(long_strings([]))