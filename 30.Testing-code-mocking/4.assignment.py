# Let's mock a fake Airport object
# Create a Mock object and assign it to a variable called 'airport'

# The airport mock should have a 'gates' attribute set to
# a list of the strings "A1", "B2", and "C3"

# The airport mock should have a "departures" attribute set to a dictionary where
# the keys are strings representing cities and the
# values are strings representing thier departure times

# {
#    "Atlanta": '12:00PM',
#    'Nashville': '04:30PM'
# }

# The airport mock should have a "close" attribute that is callable (i.e an instance method)
# when invoked, it should return the string "Closing"

# The airport should have an "open" attribute that is callable
# When invoked the first time, it should return "Opening..."
# When invoked the second time, it should return "Already open"

from unittest.mock import Mock

airport = Mock()
# airport.configure_mock(
#     gates=['A1', 'B2', 'C3'],
#     departures={'Atlanta': '12:00PM', 'Nashville': '04:30PM'}
# )

airport.gates = ['A1', 'B2', 'C3']
airport.departures = {'Atlanta': '12:00PM', 'Nashville': '04:30PM'}

airport.close.return_value = 'Closing'
airport.open.side_effect = ['Opening...', 'Already open']

print(airport.gates)
print(airport.departures)
print(airport.close())
print(airport.open())
print(airport.open())
