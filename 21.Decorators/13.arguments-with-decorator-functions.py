def be_nice(fn):
    def inner(*args, **kwargs):
        print('Nice to meet you! I\'m honored to execute your func for u')
        # print(args)
        # print(kwargs)
        fn(*args, **kwargs)
        print("It was my pleasure executing your func! have a nice day!")

    return inner


# syntatic sugar makes syntax easier
# decorator
@be_nice
def complex_business_logic(stakeholder, position):
    print(f'Something complex for our {position} {stakeholder}')


complex_business_logic('Mohamed', position='CEO')
