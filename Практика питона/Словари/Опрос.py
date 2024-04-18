favourite_languages = {
    'Eric': 'c',
    'Gibna' : 'Python',
    'gula': 'c++',
    'luke' : 'ruby',


}

persons = ['Eric', 'Gibna','gula', 'luke', 'egor' , 'dima' ]

for person in persons:
    if person in favourite_languages.keys():
        languge = favourite_languages[person]

        print(f"Спасибо за участие {person.title()}, ваш любимый язык {favourite_languages[person].title()}")
    else: print(f"Вы,{person.title()} ,еще не принимали участие")