import functools


def be_nice(fn):
    @functools.wraps(fn)
    def inner(*args, **kwargs):
        print('Nice to meet you! I\'m honored to execute your func for u')
        result = fn(*args, **kwargs)
        print("It was my pleasure executing your func! have a nice day!")
        return result

    return inner


# syntatic sugar makes syntax easier
# decorator
@be_nice
def complex_business_sum(a, b):
    """Adds two numbers together"""
    return a + b


help(complex_business_sum)
