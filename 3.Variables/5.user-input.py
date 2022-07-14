from tkinter.tix import INTEGER


name = input('What is your name: ')

print("It's nice to meet you,", name)

# Prompt the user for two numbers, one at a time
# The numbers will be received as strings
# convert both numbers to integers
# print a message that includes the sum of the two numbers

first_input = int(input("Enter first number: "))

second_input = int(input("Enter second number: "))
print("The sum of", first_input, 'and',
      second_input, 'is', first_input + second_input)
