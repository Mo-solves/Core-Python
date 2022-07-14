empty_space = "       content         "
print(empty_space)
print(len(empty_space))

# remove space in right side
print(empty_space.rstrip())
print(len(empty_space.rstrip()))

# Remove space in left side
print(empty_space.lstrip())
print(len(empty_space.lstrip()))

# clear all the spaces
print(empty_space.strip())
print(len(empty_space.strip()))

website = "www.python.org"

print(website.lstrip("w"))
print(website.lstrip("org"))
print(website.strip('worg.'))
