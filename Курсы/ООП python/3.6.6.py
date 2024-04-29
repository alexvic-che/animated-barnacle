import sys
class ShopItem:
    def __init__(self,name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))
    def __eq__(self, other):
        return hash(self) == hash(other)

lst_in = ['Системный блок: 1500 75890.56',
'Монитор Samsung: 2000 34000',
'Клавиатура: 200.44 545',
'Монитор Samsung: 2000 34000']
shop_items = {}
# i=1
# for el in lst_in:
#     lst = el.split(": ")
#     a = lst.pop(1)
#     a = a.split()
#     lst = lst + a
#
#     if ShopItem(*lst) in shop_items:
#         i+=1
#     shop_items[ShopItem(*lst)] = [ShopItem(*lst), i]


for line in lst_in:
    parts = line.split(':')
    name = parts[0].strip()
    weight, price = map(float, parts[1].strip().split())
    item = ShopItem(name, weight, price)

    if item in shop_items:
        shop_items[item][1] += 1
    else:
        shop_items[item] = [item, 1]
for key, value in shop_items.items():
    print(f"{key}: {value[0].name}, {value[1]}")