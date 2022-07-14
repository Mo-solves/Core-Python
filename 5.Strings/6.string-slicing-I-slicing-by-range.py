from email.headerregistry import AddressHeader


address = 'Attractive Street, Baverly Hills, CA 90210'

print(address[0:3])
print(address[0:4])
print(address[0:17])
print(address[19:32])
print(address[10:100])

print()

print(address[34:-6])
print(address[-8:-6])
print(address[-8:36])

print()

print(address[5:])
print(address[13:])
print(address[-10:])

print(address[:10])
print(address[0:10])
print(address[:23])
print(address[:-3])

print()

print(address[:])
