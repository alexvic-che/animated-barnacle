



def sum_list(a, b):
    new_list = []
    for el in range(len(a)):
        for el2 in range(len(b)):
            if a[el] == b[el2]:
                new_list.append(b[el2])
                print("Индекс1---- "+str(el) + " Число1---- " +str(a[el]) +" = "
                             +"Индекс2---- "+ str(el2) + " Число2---- " + str(b[el2]) )

    return new_list






a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 3]
b = [1, 7, 2, 9, 55, 1, 114, 1, 1, 55, 14,3,33,3]
result = [elem for elem in a if elem in b]
result2 = list(filter(lambda elem: elem in b, a))
result3 = list(set(a) & set(b))

print(result2)
print(result3)

