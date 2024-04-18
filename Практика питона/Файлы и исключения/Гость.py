
file = "guest.txt"
x = 0
while x<10:
    user_name = input("Введите ваше имя: ")
    hi = f"Hello {user_name}"
    print(hi)
    with open(file, 'a') as file_object:
        file_object.write(f"{hi}\n")
    x+=1

