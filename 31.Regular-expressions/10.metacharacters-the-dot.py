import re

# pattern = re.compile('e..o')
pattern = re.compile('\.')

sentence = 'hello.'

print(pattern.findall(sentence))
