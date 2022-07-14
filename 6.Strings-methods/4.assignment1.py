# Define a vowel_count function that accepts a string argument
# The function should return the count of vowels in the string
# The 5 vowels are 'a', "e", "i", "o", and "u"
# You can assume the string will be in all lowercase

def vowel_count(vowel):
    return vowel.count('a') + vowel.count('e') + vowel.count('i') + vowel.count('o') + vowel.count('u')


print(vowel_count('estate'))
print(vowel_count('helicopter'))
print(vowel_count('ssh'))

print()
# Define a find_my_letter function that accepts two arguments: a string and a character
# The function should return the first index position of the character in the string
# The function should return a -1 if the character does not exist in the string


def find_my_letter(string, letter):
    return string.find(letter)


print(find_my_letter('dangerous', 'a'))
print(find_my_letter('bazooka', 'z'))
print(find_my_letter('lollipop', 'z'))
