# name, adjective, noun
# mad_libs = "{} laughed at the {} {}."

# first way
# print(mad_libs.format('Mohamed', 'green', 'alien'))
# print(mad_libs.format("Jennifer", "silly", 'tomato', 'fsdfjsdhfjk'))

# second way
# mad_libs = "{2} laughed at the {1} {0}."

# print(mad_libs.format('Mohamed', 'green', 'alien'))
# print(mad_libs.format("Jennifer", "silly", 'tomato', 'fsdfjsdhfjk'))

# third way
mad_libs = "{name} laughed at the {adjective} {noun}."

# print(mad_libs.format(name='Mohamed', adjective='green', noun='alien'))
# print(mad_libs.format(name="Jennifer", adjective="silly", noun='tomato'))

name = input("Enter a name: ")
adjective = input('Enter an adjective: ')
noun = input('Enter a noun: ')

print(mad_libs.format(name=name, adjective=adjective, noun=noun))
