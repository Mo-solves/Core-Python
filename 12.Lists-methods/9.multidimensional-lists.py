bubble_tea_flowers = [
    ["Honey", "Mango", "Passion Fruit"],
    ['Peach', 'Plum', 'Strawberry', 'Taro'],
    ['Kiwi', 'Chocolate']
]

# print(len(bubble_tea_flowers))
# print(bubble_tea_flowers[0][0])
# print(bubble_tea_flowers[1][2])

all_flavors = []

for flavor_pack in bubble_tea_flowers:
    for flavor in flavor_pack:
        all_flavors.append(flavor)

print(all_flavors)
