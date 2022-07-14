# Declare a months tuple with the last 4 months of the year
# (September, October, November, December) as strings
# Make sure the first letter of each month is capitalized

months = ('September', 'October', 'November', 'December')
print(months)

# Create a faves variabl with a list of your 3 favorite movies as strings
# Use the tuple function to convert the list to a tuple and
# save the result in a movies variable

faves = ['One Piece', 'Bleach', 'Naruto']
movies = tuple(faves)
print(movies)

# Create a numbers_a, numbers_b, and numbers_c  tuples
# Each tuple should contain 3 integers
# Declare an all_numbers tuple containing these three tuples

numbers_a = (1, 2, 3)
numbers_b = (4, 5, 6)
numbers_c = (7, 8, 9)

all_numbers = (numbers_a, numbers_b, numbers_c)
print(all_numbers)
