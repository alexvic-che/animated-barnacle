numbers = list(range(1, 10))
print(numbers)

for number in numbers:
    if number >= 1  and number<4:
        if number == 1:
            print('1st')
        if number == 2:
            print('2nd')
        if number == 3:
            print("3rd")
    else: print(f"{number}th")
