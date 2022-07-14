errands = ['Go to gym', 'Grab lunch', 'Get promoted at work', 'Sleep']

# enumerate function
print(enumerate(errands))

for index, errand in enumerate(errands, 1):
    print(f'{errand} is number {index} on my list of things to do today!')
