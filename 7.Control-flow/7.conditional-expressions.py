from tabnanny import check


zip_code = '90210'

# check
# if len(zip_code) == 5:
#     check = 'Valid'
# else:
#     check = 'Invalid'


# Ternary operator
check = "Valid" if len(zip_code) == 5 else 'Invalid'

print(check)
