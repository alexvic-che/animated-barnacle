def sum (a, b):
    sum = a+b
    return sum
while True:
    try:
        first_number = int(input("Введите первое число"))
        second_number = int(input("Введите второе число"))
    except ValueError:
        print("Вы ввели не число")
    else:
        print(sum(first_number, second_number))



