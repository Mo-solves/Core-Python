# Declare a PizzaPie class that accepts a total_slices parameter
# In the instantiation process for an object, assign the parameter
# to an attribute with the same name

# A PizzaPie object should also be initialized with a _slices_eaten
# protected attribute set to 0

# Define a slices_eaten property
# The getter method should retrieve the value of the _slices_eaten
# The setter method should set a new value for the _slices_eaten
# but only if the argument is less than total_slices
class PizzaPie():
    def __init__(self, total_slices):
        self.total_slices = total_slices
        self._slices_eaten = 0

    @property
    def slices_eaten(self):
        return self._slices_eaten

    @slices_eaten.setter
    def slices_eaten(self, slices_eaten):
        if slices_eaten < self.total_slices:
            self._slices_eaten = slices_eaten

    # def _get_slices(self):
    #     return self._slices_eaten

    # def _set_slices(self, slices_eaten):
    #     if slices_eaten < self.total_slices:
    #         self._slices_eaten = slices_eaten

    # slices_eaten = property(_get_slices, _set_slices)

    @property
    def percentage(self):
        return self._slices_eaten / self.total_slices


cheese = PizzaPie(8)
cheese.slices_eaten = 2
print(cheese.percentage())

cheese.slices_eaten = 4
print(cheese.percentage())

cheese.slices_eaten = 10
print(cheese.percentage())
