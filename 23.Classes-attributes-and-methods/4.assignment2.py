# Let's say we want to model a Book as a Python object
# A Book has an author and a publisher, which are characteristics
# that cannot change
# A Book also has a page_count, which could be altered if you rip some
# pages from the book

# Declare a Book class that accepts author, publisher, and page_count para
# Each of the parameters should be assigned to an attribute
# The author and publisher attributes should be designated as protected
# The page_count attribute should be designated public

# Define a copyright instance method that returns a string with information about the copyrights
# It should look the string below, where "Grand Cardone" is the value of the protected author attribute and "10x Entrerprises" is the value of the protected publisher attribute

# => Copyright Grant Carbone, 10X Enterprise

# The public page_count attribute can always be manually modified
# However, we can still define an instance method that modifies it

# Declare a rip_in_half instance method
# If the book has more than 1 page, it should halve the page_count
# If the book has 1 page or less, it should set the page_count to 0

class Book():
    def __init__(self, author, publisher, page_count):
        self._author = author
        self._publisher = publisher
        self.page_count = page_count

    def copyright(self):
        return f'Copyright {self._author}, {self._publisher}'

    def rip_in_half(self):
        if self.page_count > 1:
            self.page_count /= 2
        elif self.page_count <= 1:
            self.page_count = 0


book = Book(author='Grand Cardone', publisher='10X Enterprise', page_count=10)

print(book.copyright())

print(book.page_count)
book.rip_in_half()
book.rip_in_half()
book.rip_in_half()
book.rip_in_half()
print(book.page_count)
