from random import choice

ns =[23, 43, 5 ,4 ,'s', 67, 'b', 62, 'j', 89, 'q', 76, 'e', 7, 90 ]
x=1

while x<=1000000000:
    prokrut = [choice(ns), choice(ns),choice(ns),choice(ns),choice(ns)]
    print(f"Ваша комбинация: {prokrut}" )
    if prokrut == ['s', 's', 's', 's',"s"]:
        print("You win")
        print(x)
        break

    x+=1


