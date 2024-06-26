class Recipe:
    def __init__(self, *args):
        self.ingridients = [*args]

    def add_ingredient(self, ing):
        self.ingridients.append(ing)
    def remove_ingredient(self, ing):
        self.ingridients.remove(ing)
    def get_ingredients(self):
        return tuple(self.ingridients)

    def __len__(self):
        return len(self.ingridients)

class Ingredient:

    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure
    def __str__(self):
        return f"{self.name}: {self.volume}, {self.measure}"


recipe = Recipe()
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
ings = recipe.get_ingredients()
n = len(recipe) # n = 3
for ing in ings:
    print(ing)
print(n)
