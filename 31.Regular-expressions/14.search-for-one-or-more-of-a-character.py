import re

pattern = re.compile('\d+\s+\d+\s+\d+')

sentence = "I can be reached at 555 123 4567 and I'd appreciate a call tomorrow, Again, my number is 555 123 4567. Thank you."

print(pattern.findall(sentence))
