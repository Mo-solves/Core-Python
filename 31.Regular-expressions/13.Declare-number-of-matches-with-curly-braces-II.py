import re

pattern = re.compile('\s{3}')

sentence = 'hello   goodbye'

print(pattern.findall(sentence))

sentence = '123 4567 789 01'

pattern = re.compile('\d{4}')

print(pattern.findall(sentence))

sentence = "I can be reached at 555-123-4567 and I'd appreciate a call tomorrow, Again, my number is 555-123-4567. Thank you."

pattern = re.compile('\d{3}-\d{3}-\d{4}')

print(pattern.findall(sentence))

sentence = "I can be reached at 555 123 4567 and I'd appreciate a call tomorrow, Again, my number is 555 123 4567. Thank you."

pattern = re.compile('\d{3}\s\d{3}\s\d{4}')
print(pattern.findall(sentence))
