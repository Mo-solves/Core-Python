# Assign a list of four dictionaries to a "complexity" variable below

# The first and third dictionaries should have two key_value pairs
# For those dictionaries, the key should be strings and the values should be Booleans

# The second and fourth dictionaries should have three key-value pairs
# For those dictionaries, the keys should be floats
# and the values should be list of strings
# The lists can be of any length

complexity = [
    {'isOlder': False, 'isCooking': False},
    {3.14: 'PI', 36.5: 'normal temperature', 100: 'full score'},
    {'Graduated': True, 'Programmer': False},
    {12.5: 'good number', 10.6: 'price of cake', 1.56: 'price of gas'}
]

for my_dict in complexity:
    for key, value in my_dict.items():
        print(f'Key is {key} and the value is {value}')
