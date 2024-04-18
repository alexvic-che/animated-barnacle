import json
number = input("Inter ur favourite number: ")
file = "favourite_user_number.json"


with open(file, 'w') as f:
    json.dump(number, f)

with open(file) as f:
    favourite_number = json.load(f)
    print(f"I know ur favoutite number {favourite_number}")