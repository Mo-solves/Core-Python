# Define a fancy_cleanup function that accepts a single string argument
# The function should clean up the whitespaces on both sides of the argument
# it should also replace every occurance of the letter "g" with the letter "z"
# and every occurance of a space with an exclamation pont (!).

def fancy_cleanup(string):
    return string.strip().replace('g', 'z').replace(' ', '!')


print(fancy_cleanup("       geronimo crikey  "))
print(fancy_cleanup("       nonsense "))
print(fancy_cleanup("grade"))
