animals = ['elephant', 'horse', 'cat', 'giraffe', 'cheetah', 'dog']


def length_greater_than_five(animal):
    return len(animal) > 5


print(list(filter(length_greater_than_five, animals)))
