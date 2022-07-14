# Closure is a programming pattern in which a scope retains acces to
# an enclosing scope's names

def auter():
    candy = 'Snickers'

    def inner():
        return candy

    return inner


the_func = auter()

print(the_func())
