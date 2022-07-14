# Declare a plenty_0f_arguments function that accepts two parameters (a and b) and an additional **kwargs parameter

# The function should return True if the sum of a, b, and the values of
# **kwargs is greater than 100. It should return false otherwise
#
def plenty_arguments(a, b, **kwargs):
    # total = 0
    # total_dict = 0
    # for value in kwargs.values():
    #     total_dict += value
    # total = (a + b) + total_dict
    # if total > 100:
    #     return True
    # return False
    return a + b + sum(kwargs.values()) > 100


print(plenty_arguments(20, 30))
print(plenty_arguments(a=50, b=75))
print(plenty_arguments(a=50, b=25, c=50))
print(plenty_arguments(a=25, b=25, c=25, d=25))
print(plenty_arguments(a=25, b=25, c=25, d=26))
