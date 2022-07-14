# Given the tuple below, destructure the three values and
# assign them to position, city and salary variables
# Do NOT use index position (i.e job_opening[1])
job_opening = ['Software Engineer', 'New York City', 100000]

position, city, salary = job_opening
print(position, city, salary)

# Given the tuple below,
# - destructure the first value and assign it to a street variable
# - destructure the last value and assign it to a zip_code variable
# - destructure the middle two value into  a list and assign it to a city_and_state variable
address = ['35 Elm Street', 'San Francisco', 'CA', '94107']

street, *city_and_state, zip_code = address
print(street, city_and_state, zip_code)

# Declare a sum_of_evens_and_odds function that accepts a tuple of numbers
# It should return a tuple with two numeric values:
# -- the sum of the even numbers
# -- the sum of the odd numbers


def sum_of_evens_and_odds(numbers):
    odd = 0
    even = 0
    for number in numbers:
        if number % 2 == 0:
            even += number
        elif number % 2 != 0:
            odd += number
    result = (even, odd)
    return result


print(sum_of_evens_and_odds((1, 2, 3, 4)))
print(sum_of_evens_and_odds((1, 3, 5)))
print(sum_of_evens_and_odds((2, 4, 6)))
