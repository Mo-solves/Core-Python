if 5 < 7 and 'rain' == 'rain':
    print("Both of these consitions evaluate to true")

if 5 < 7 and 'rain' == 'fire':
    print("This will not print coz at least one of the conditions is false")

if 'rain' == 'fire' and 5 < 7:
    print("This will not print coz at least one of the conditions is false")

if 'rain' == 'fire' and 5 > 7:
    print("This will not print coz at least one of the conditions is false")

value = 95

# if value > 90 and value < 100:
if 90 < value < 100:
    print("This is a shortcut for the win!")
