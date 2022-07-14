# Define an invoke_thrice function
# It should accept a single argument (which will be a function)
# In its body, the invoke_thrice function should invoke
# the function that's passed in exactly three times

def greeting():
    print('Hello My friend')


def invoke_thrice(func):
    func()
    func()
    func()


invoke_thrice(greeting)
