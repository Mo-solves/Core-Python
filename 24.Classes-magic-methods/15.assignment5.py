# Declare a Newspaper class

# Each Newspaper will have a "pages" attribute set to an integer
# and a "section" attribute set to a dictionary
# The key in "sections" will be strings representing a section (i.e "Politics")
#

# The length of a newspaper should be equal to the number of pages it holds

# Indexing the newspaper by a section should return the starting page for that section

# Make it so two newspapers are considered equal if they have the
# same number of pages AND same number of sections

from tkinter import PAGES


monday_sections = {
    'Politics': 'A5',
    'Sports': 'B2',
    'Entertainment': 'C3'
}

tuesday_sections = {
    'Travel': 'A5',
    'Cooking': 'B2'
}

wednesday_sections = {
    'Classifieds': 'A5',
    'Weddings': 'B2',
    'Weather': 'C3'
}


class Newspaper():
    def __init__(self, pages, sections):
        self.pages = pages
        self.sections = sections

    def __len__(self):
        return self.pages

    def __getitem__(self, index):
        return self.sections[index]

    def __eq__(self, other_newspaper):
        equal_pages = self.pages == other_newspaper.pages
        equal_sections = len(self.sections) == len(other_newspaper.sections)
        return equal_pages and equal_sections


np1 = Newspaper(pages=80, sections=monday_sections)
np2 = Newspaper(pages=60, sections=tuesday_sections)
np3 = Newspaper(pages=80, sections=wednesday_sections)

print(len(np1))
print(len(np2))
print(np1 == np2)
print(np1 == np3)
print(np1['Politics'])
print(np2['Cooking'])
