def positive_or_negative(number):
    if number > 0:
        return 'Positive'
    elif number < 0:
        return 'Negative'
    else:
        return 'Neither! It\'s zero'


print(positive_or_negative(5))
print(positive_or_negative(-3))
print(positive_or_negative(0))


def calculator(operation, a, b):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        return a / b
    else:
        return 'Not a valid operation'


print(calculator('add', 10, 8))
print(calculator('subtract', 10, 8))
print(calculator('multiply', 10, 8))
print(calculator('divide', 10, 8))
print(calculator('hello', 10, 8))
