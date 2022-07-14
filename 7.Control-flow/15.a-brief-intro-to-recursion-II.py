# def reverse(str):
#     last_index = len(str) - 1
#     reversed_string = ''

#     while last_index >= 0:
#         reversed_string += str[last_index]
#         last_index -= 1

#     return reversed_string

def reverse(str):
    # basecase
    if len(str) <= 1:
        return str

    return str[-1] + reverse(str[:-1])


print(reverse('straw'))
print(reverse("Hello"))
print(reverse("Mohamed"))
