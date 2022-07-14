# pillows = {
#     'soft': 79.99,
#     'hard': 99.99
# }

# print(pillows['soft'])
# print(pillows.__getitem__('hard'))

class CrayonBox():
    def __init__(self):
        self.cryanos = []

    def add(self, cryon):
        self.cryanos.append(cryon)

    def __getitem__(self, index):
        return self.cryanos[index]

    def __setitem__(self, index, value):
        self.cryanos[index] = value


cb = CrayonBox()
cb.add('Blue')
cb.add('Red')

print(cb[0])
print(cb[1])

cb[0] = 'Yellow'
print(cb[0])

for crayon in cb:
    print(crayon)
