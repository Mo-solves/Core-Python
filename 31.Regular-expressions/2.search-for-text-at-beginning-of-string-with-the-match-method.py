import re

pattern = re.compile('flower')

# match looks only at the beginnig of the sentence
match = pattern.match('flower power')

if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())
