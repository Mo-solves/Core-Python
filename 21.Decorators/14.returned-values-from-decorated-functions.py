def be_nice(fn):
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
    return a + b


print(complex_business_sum(3, 5))
