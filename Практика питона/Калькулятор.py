def arithmetic (number1, number2, symbol):
    if symbol == "+":
        res = number1 + number2
        return res
    if symbol == "-":
        res = number1 - number2
        return float(res)
    if symbol == "/":
        if number2 == 0:
            return print("На ноль делить нельзя")
        else:
            res = number1 / number2
            return res
    if symbol == "*":
        res = number1 * number2
        return res
    return print("Некорректно выбранная операция")

def isDigit_number1():
    while True:
        try:
            number1 = float(input("Ввдeите первое число: "))
            return number1
        except ValueError:
            print("Введите число")

def isDigit_number2():
    while True:
        try:
            number2 = float(input("Ввeдите второе число: "))
            return number2
        except ValueError:
            print("Введите число")


def Symbol():
    symbol = input("Ввдите операцию: + - / *: ")
    return symbol



print(arithmetic(isDigit_number1(), isDigit_number2(), Symbol()))



