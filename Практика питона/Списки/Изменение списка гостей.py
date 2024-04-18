names_for_dinner = ['lial', 'egorm','andrue']

print(f"I send you, {names_for_dinner[0].title()}, to dinner")
print(f"I send you, {names_for_dinner[1].title()}, to dinner")
print(f"I send you, {names_for_dinner[2].title()}, to dinner")

print(f"{names_for_dinner[2].title()}, not to go to me")

del names_for_dinner[2]

names_for_dinner.append("danik")
print(f"I send you, {names_for_dinner[0].title()}, to dinner")
print(f"I send you, {names_for_dinner[1].title()}, to dinner")
print(f"I send you, {names_for_dinner[2].title()}, to dinner")
