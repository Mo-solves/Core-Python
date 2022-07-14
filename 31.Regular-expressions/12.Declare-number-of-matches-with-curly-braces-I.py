import re

# occurance of a character exactly 3
pattern = re.compile('z{3}')

sentence = 'zzz zzz zz zzzz'

print(pattern.findall(sentence))

# occurance of a row characters 3 or more
pattern = re.compile('z{3,}')
print(pattern.findall(sentence))
