def accept_stuf(*args):
    print(type(args))
    print(args)


accept_stuf(1)
accept_stuf(1, 3, 5)
accept_stuf(1, 2, 3, 4, 5)
accept_stuf()


def my_max(*numbers, nonsense):
    print(nonsense)
    max_number = numbers[0]
    for number in numbers:
        if max_number < number:
            max_number = number
    return max_number


print(my_max(1, nonsense='xaad tidhi'))
print(my_max(1, 3, 4, 8, nonsense='yaa'))
