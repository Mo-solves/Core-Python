# Define an encrypt_message function that accepts a string
# The input string will consist of only alphabetic characters.
# The function should return a string where all characters have been moved
# "up" two spots in the alphabet . for example, "a" will become "c"

def encrypt_message(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encripted = ''
    for letter in message:
        encrypted_letter_index_position = (alphabet.index(letter) + 2) % 26
        encripted += alphabet[encrypted_letter_index_position]
    return encripted


print(encrypt_message('abc'))
print(encrypt_message('xyz'))
print(encrypt_message('mno'))
print(encrypt_message('pqr'))
print(encrypt_message('zab'))
print(encrypt_message('wxy'))

# 5 % 3 ==> 2
# 3 % 5 ==> 3
