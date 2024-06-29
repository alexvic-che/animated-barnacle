def get_sum(mas, target):
    for i, el in enumerate(mas):
        j = i
        while j<len(mas):
            if j==i:
                j += 1
                continue
            if el+mas[j]==target:
                return [i,j]
            j+=1


nums = [3,3]

target = 5

print(get_sum(nums, target))
