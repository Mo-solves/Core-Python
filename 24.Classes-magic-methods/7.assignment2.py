# Define a CollegeStudent class that accepts and assigns a university attribute
# Add a docstring for the class equal to "Blueprint for a student at an institution of higher"

# define three instance methods - sleep, eat, and party
# The actual content of the methods is irrelevent (feel free to use the pass keyword)

# The sleep method should have the docstring "Sleep through class"
# The eat method should have the docstring "Go to cafeteria"
# The party method should have the docsting "Hit the books hard"

# To simplify the test evaluation, submit all docstring without any line break
# You're welcome to use single quotes, double quotes, or triple quotes

class CollegeStudent():
    'Blueprint for a student at an institution higher'

    def __init__(self, college):
        self.college = college

    def sleep(self):
        "Sleep through class"
        pass

    def eat(self):
        """Go to cafeteria"""
        pass

    def party(self):
        """Hit the books hard"""
        pass


print(CollegeStudent.__doc__)

marty = CollegeStudent('Python Community College')
print(marty.sleep.__doc__)
print(marty.eat.__doc__)
print(marty.party.__doc__)
