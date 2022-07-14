powerball_numbers = [4, 8, 15, 16, 23, 42]

def squares(numbers):
    square_numbers = []
    for number in numbers:
        square_numbers.append(number ** 2)
    return square_numbers

print(squares(powerball_numbers))

def convert_to_floats(numbers):
    floats = []
    for number in numbers:
        floats.append(float(number))
    return floats

print(convert_to_floats(powerball_numbers))

def even_or_odd(numbers):
    even_or_odd = []
    for number in numbers:
        if number % 2 == 0:
            even_or_odd.append(True)
        else:
            even_or_odd.append(False)
    return even_or_odd

print(even_or_odd(powerball_numbers))