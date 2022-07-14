import re

# include charcters
pattern = re.compile('[wfr]')

sentence = 'flower power'

print(pattern.findall(sentence))

# except charcteres
pattern = re.compile('[^wfr]')

print(pattern.findall(sentence))

# range
pattern = re.compile('[a-l]')
print(pattern.findall(sentence))
