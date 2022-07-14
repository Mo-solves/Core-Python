capitals = {
    'New York': 'Albany',
    'California': 'Sacramento',
    'Texas': 'Austin'
}

inverted = {capital: state for state,
            capital in capitals.items() if len(capital) != len(state)}
print(inverted)
