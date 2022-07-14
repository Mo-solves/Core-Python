# LEGB stands for
# Local-Enclosing functions-Global-Built in

# Global scope
# x = 15


def auter():
    # Enclosing function scope
    # x = 10

    def inner():
        # local scope
        # x = 5
        return len  # built in scope

    return inner()


print(auter()('Python'))
