age = 28


def fancy_func():
    # shadow variable a variable that shares the same name as global variable
    age = 100
    print(age)


fancy_func()
print(age)

# constant variables

TAX_RATE = 0.06


def calculate_tax(price):
    return round(price * TAX_RATE, 2)


def calculate_tip(price):
    return round(price * (TAX_RATE * 3), 2)


print(calculate_tax(10))
print(calculate_tip(10))
