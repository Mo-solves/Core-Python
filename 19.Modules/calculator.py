creator = 'Mohamed'
PI = 3.14159


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def area(radius):
    return PI * radius * radius


# varibale which start with underscore _ are not imported
_year = 2022

if __name__ == '__main__':
    print('This will only run when calculator is being executed as a script')
    print(subtract(3, 5))
