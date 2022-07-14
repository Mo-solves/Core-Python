values = [3, 6, 9, 12, 15, 18, 21, 24]
other_values = [5, 10, 15, 20, 25, 30]


def odds_sum(numbers):
    total = 0

    for number in numbers:
        if not number % 2 == 0:
            total += number

    return total


print(odds_sum(values))
print(odds_sum(other_values))

print()


def largest_number(numbers):
    largest = numbers[0]
    for number in numbers:
        if largest < number:
            largest = number
    return largest


print(largest_number(values))
print(largest_number(other_values))
print(largest_number([1, 2, 3]))
print(largest_number([3, 2, 1]))
print(largest_number([4, 5, 5]))
print(largest_number([-3, -2, -1]))
