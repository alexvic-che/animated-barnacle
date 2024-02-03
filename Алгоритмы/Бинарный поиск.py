def binary_search(list, item):
    low=0
    high= len(list)-1
    while low <= high:
        mid = (low+high)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid-1
        else:
            low = mid+1

    return None

s=[]
print(s)
for i in range(1,11):
    s.append(i)

print(s)
my_list = [1, 3, 5, 7, 9, 11, 103, 643, 1034]
print(binary_search(s, 10))


