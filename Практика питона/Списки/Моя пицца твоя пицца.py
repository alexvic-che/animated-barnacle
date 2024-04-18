my_pizzas = ["pepperoni", "gavaiskay", "chili"]
friend_pizzas = my_pizzas[::]

friend_pizzas.append('ciplenok')
my_pizzas.append('barbeq')

print(f"My favourite pizzas : {my_pizzas}")
print(f"My friend favourite pizzas : {friend_pizzas}")

for pizzas in my_pizzas:
    print(pizzas)

for pizzas in friend_pizzas:
    print(pizzas)
