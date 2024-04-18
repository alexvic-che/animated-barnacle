country_names = ['rusiia', 'germany', 'america', 'engaldnd', 'scotland']
print(country_names)

#Вывод в алфавитном порядке(временный)

print(sorted(country_names))

#Показывает  что список не меняется а тольео выводится в алфавитном порядке
print(country_names)

print(sorted(country_names, reverse=True))

print(country_names)

#Переворт списка
country_names.reverse()
print(country_names)
country_names.reverse()
print(country_names)

country_names.sort()
print(country_names)
country_names.sort(reverse=True)
print(country_names)