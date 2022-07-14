file_name = 'My_first_file.txt'

# write a file
with open(file_name, 'w') as file_object:
    file_object.write("Hello file!\n")
    file_object.write('You are my favorite file')

# read file
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())
