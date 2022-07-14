# Define a function that iterates over a list of numbers
# multiplies each number by one less than its index position
# and returns the total sum of those products

numbers = [1, 5, 2, 4, 8, 9, 12, 20]


def multiply_element_by_one_less_than_index(numbers):
    multiply = 0
    sum = 0
    for index, number in enumerate(numbers):
        multiply = number * (index-1)
        sum += multiply

    return sum


final_result = multiply_element_by_one_less_than_index(numbers)
print(final_result)
