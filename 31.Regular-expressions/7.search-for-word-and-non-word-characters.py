import re

pattern = re.compile('\w')

sentence = 'I went to the store and bought 5 apples, 4 oranges, and 15 plums.'

print(pattern.findall(sentence))

pattern = re.compile('\W')
print(pattern.findall(sentence))
