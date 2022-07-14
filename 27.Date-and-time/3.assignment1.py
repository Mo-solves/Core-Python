from datetime import date, time
# Declare a titanic variable pointing to a date object representing April 14th, 1912
titanic = date(year=1912, month=4, day=14)
print(titanic)

# Declare an independence_day variable pointing to a date object representing July 4th, 1776
independence_day = date(year=1776, month=7, day=4)
print(independence_day)

# Declare an alarm_clock variable set to a time object representing 05:45:00AM
alarm_clock = time(hour=5, minute=45)
print(alarm_clock)

# Declare a one_second_away variable set to a time object representing 11:59:59PM
one_second_away = time(hour=23, minute=59, second=59)
print(one_second_away)
