cities ={
    "Moskoy":{
        'city_country' : 'Russia',
        "population" : 123134,
        "fact": "hes beautifel"
    },
    "newyork":{
        'city_country' : 'Americqa',
        "population" : 121424144,
        "fact": "hes small"
    },

    "paris":{
        'city_country' : 'France',
        "population" : 313415,
        "fact": "hes duma"
    },
}

for city, info in cities.items():
    print(f"{city} ")
    print(f"Information: {info} ")