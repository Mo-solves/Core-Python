# Define an "auter" function that accepts no arguments
# Inside the body of "auter", define an "inner" function
# The "inner" function should return the value 5
# From "outer", return the uninvoked "inner" function
def auter():
    def inner():
        return 5

    return inner


print(auter()())
