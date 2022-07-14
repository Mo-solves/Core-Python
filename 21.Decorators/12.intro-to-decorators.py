def be_nice(fn):
    def inner():
        print('Nice to meet you! I\'m honored to execute your func for u')
        fn()
        print("It was my pleasure executing your func! have a nice day!")

    return inner


# syntatic sugar makes syntax easier
# decorator
@be_nice
def complex_business_logic():
    print('Something complex')


@be_nice
def another_fancy_function():
    print('Goo goo gaga')


# complex_business_logic()
another_fancy_function()
# be_nice(complex_business_logic)()
