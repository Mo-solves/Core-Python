# You are writing a Python program to model a remove control
# for a television set. Declare a stations_to_numbers
# function that accepts a dictionary. The keys will be
# channel numbers and the values will be the station names

channels = {
    2: 'CBS',
    4: 'NBC',
    5: 'FOX',
    7: 'ABC'
}
# The station_to_numbers function should return an
# inverted dictionary where the keys are the station names
# and the values are the channel numbers


def station_to_numbers(my_dict):
    return {station: channel for channel, station in my_dict.items()}


print(station_to_numbers(channels))

# Declare a coaster_conversion function that accepts a dictionary
# The keys of the dictionary will be strings representing roller coasters
# The values will be the heights of each coaster in meters
#
# Return a new dictionary with the same keys
# The values should be the heights converted from meters to feet,
# The final values (in feet) should also be rounded to the closest integer
# HINT: 1 meter is equal to 3.28084 feet
# HINT: The round function rounds a number to the nearest integer

coasters = {
    'Kingda Ka': 139,
    'Top Thrill Dragster': 130,
    'Superman: Escape from krypton': 126
}


def coaster_conversion(my_dict):
    return {key: int(value * 3.28084) for key, value in my_dict.items()}


print(coaster_conversion(coasters))
