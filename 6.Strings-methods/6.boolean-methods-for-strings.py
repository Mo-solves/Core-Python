season = 'winter'
print(season.islower())

season = 'Winter'
print(season.islower())

season = 'SUMMER'
print(season.isupper())

season = 'sUMMER'
print(season.isupper())

print("The Four Seasons".istitle())
print("The 4 Season".istitle())
print("The four Seasons".istitle())

print("area".isalpha())
print("Area 51".isalpha())

print("51".isnumeric())
print("Area 51".isnumeric())

print("Area51".isalnum())
print("Area 51".isalnum())

print(" ".isspace())
print("   ".isspace())
print(" 5 ".isspace())
print(" k ".isspace())
print(" ! ".isspace())
