# Define a function called "factorial" that accepts a single number as input
#
# A factorial represents the product of all numbers up to, and including, that number
# for example, 5 factorial 5*4*3*2*1 = 120
#
# Return the factorial calculation from your function. You should NOT use any kinds of loops
# Instead, utilize recursion. Your function Must call itself

def factorial(number):
    # basecase
    if number == 1:
        return number

    return number * factorial(number - 1)


print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
