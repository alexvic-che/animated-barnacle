active =1

while active<7:
        age = input("Введите возравст:")
        if age.isdigit():
            if int(age) < 3:
                print('Билет бесплатный')

            if int(age) >= 3 and int(age)<12:
                print('Билет стоит 10 баксов')


            if int(age) >=12:
                print('Билет стоит 15 баксов')
        else:
            if age.title() == "Quit":
                break
            else: print("вы ввели недопустимый символ")

        active+=1