def countdown(i):
    print(i)
    if i<=0:
        return
    else:
        countdown (i-1)

def greet(name):
    print("hello "+ name)
    greet2(name)
    print("getting ready to say bye")
    bye()



def greet2(name):
    print("how are you " + name)
def bye():
    print("ok bye")



def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)




print(factorial(152))

def sum(arr):#Функция для суммы элементов массива без рекурсии
    total=0
    for x in arr:
        total +=x
    return total

arr=[1,5,-3,10]

def recurseve_sum(arr):#Функция для суммы элементов массива
    if arr == []:
        return 0
    return arr[0]+recurseve_sum(arr[1:])

print(recurseve_sum(arr))

def count(arr):#Функция для подсчета элементов в массиве
    if arr==[]:
        return 0
    return 1+count(arr[1:])
print(count(arr))

