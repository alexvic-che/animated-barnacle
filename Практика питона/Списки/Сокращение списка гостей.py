names_for_dinner = ['lial', 'egorm','andrue']

print(f"I send you, {names_for_dinner[0].title()}, to dinner")
print(f"I send you, {names_for_dinner[1].title()}, to dinner")
print(f"I send you, {names_for_dinner[2].title()}, to dinner""\n")

print(f" Я пригласил {len(names_for_dinner)} людей")
print(f"{names_for_dinner[2].title()}, not to go to me""\n")

del names_for_dinner[2]

names_for_dinner.append("danik")
print(f"I send you, {names_for_dinner[0].title()}, to dinner")
print(f"I send you, {names_for_dinner[1].title()}, to dinner")
print(f"I send you, {names_for_dinner[2].title()}, to dinner""\n")

print("I buy a new table and for this I widther my send list""\n")

names_for_dinner.insert(0, "dimka")
names_for_dinner.insert(2, "timbys")
names_for_dinner.append("vlad")

print(f"I send you, {names_for_dinner[0].title()}, to dinner")
print(f"I send you, {names_for_dinner[1].title()}, to dinner")
print(f"I send you, {names_for_dinner[2].title()}, to dinner")
print(f"I send you, {names_for_dinner[3].title()}, to dinner")
print(f"I send you, {names_for_dinner[4].title()}, to dinner")
print(f"I send you, {names_for_dinner[5].title()}, to dinner""\n")

print("Post dont to get me a new table in time and for this situation i sen a two person""\n")

print(f"{names_for_dinner.pop().title()}, my regretions")
print(f"{names_for_dinner.pop().title()}, my regretions")
print(f"{names_for_dinner.pop().title()}, my regretions")
print(f"{names_for_dinner.pop().title()}, my regretions""\n")

print(f"I send you, {names_for_dinner[0].title()}, to dinner")
print(f"I send you, {names_for_dinner[1].title()}, to dinner")

names_for_dinner.remove('dimka')
names_for_dinner.remove('lial')
print(names_for_dinner)


