# Define a one_from_two function that accepts a date object and a time object
# It should return a datetime object consisting of
#   - the year, month and day from date object
#   - the hour, minutes, and seconds from the time object

from datetime import date, time


def one_from_two(date, time):
    return f'datetime object representing {date} {time}'


some_date = date(2002, 2, 22)
some_time = time(9, 45, 23)

print(one_from_two(some_date, some_time))
