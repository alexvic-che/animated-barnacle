lakes_countey = {
    'nile':'egypt',
    'elens':'rusiia',
    'volga':'rusia',

}

for lake, country in lakes_countey.items():
    print(f"The {lake.title()} runs through {country.title()}")

for lake in lakes_countey.keys():
    print(f"Lake : {lake.upper()}")

for country in lakes_countey.values():
    print(f"Country: {country.upper()}")