# Write a factors function that accepts a positive whole number
# It should return a list of all of the number's factors in ascending order
# HINT: Could the range function be helpful here? Or maybe a while loop?

def factors(number):
    start = 1
    factors = []
    while start <= number:
        if number % start == 0:
            factors.append(start)
        start += 1
    return factors

print(factors(1))
print(factors(2))
print(factors(10))
print(factors(64))