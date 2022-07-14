import re

pattern = re.compile('\s')

sentence = 'I went to the store and bought 5 apples, 4 oranges, and 15 plums.'

print(pattern.findall(sentence))

pattern = re.compile('\S')
print(pattern.findall(sentence))
